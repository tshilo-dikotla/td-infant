from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_appointment.constants import IN_PROGRESS_APPT
from edc_constants.constants import BY_BIRTH
from edc_registration.models import RegisteredSubject

from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from td_maternal.models.karabo_subject_consent import KaraboSubjectConsent

from ..models import InfantBirth
from .infant_appointment import Appointment
from .infant_visit import InfantVisit


@receiver(post_save, weak=False, sender=InfantBirth,
          dispatch_uid='infant_birth_on_post_save')
def infant_birth_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this infant birth, if
    it does not exist.
    """
    if not raw:
        # Update infant registered subject
        try:
            registered_subject = RegisteredSubject.objects.get(
                subject_identifier=instance.subject_identifier)
        except RegisteredSubject.DoesNotExist:
            raise ValidationError(
                f'Missing registered subject for {instance.subject_identifier}')
        else:
            registered_subject.first_name = instance.first_name
            registered_subject.initials = instance.initials
            registered_subject.dob = instance.dob
            registered_subject.gender = instance.gender
            registered_subject.registration_datetime = instance.report_datetime
            registered_subject.registration_status = BY_BIRTH
            registered_subject.registration_identifier = instance.pk
            registered_subject.save()
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model='td_infant.onscheduleinfantbirth',
                name=instance.schedule_name)
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model='td_infant.onscheduleinfantbirth',
                name=instance.schedule_name)
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.report_datetime)


@receiver(post_save, weak=False, sender=KaraboSubjectConsent,
          dispatch_uid='resave_infant_visit_on_post_save')
def resave_infant_visit_on_post_save(sender, instance, raw, created, **kwargs):
    """Resaves infant visit, after karabo consent save to
    run the rule groups.
    """
    if created:
        try:
            maternal_reg_subject = RegisteredSubject.objects.get(
                subject_identifier=instance.subject_identifier)
            infant_reg_subject = RegisteredSubject.objects.get(
                relative_identifier=maternal_reg_subject.subject_identifier)
        except RegisteredSubject.DoesNotExist:
            raise ValidationError(
                f'Missing registered subject for {instance.subject_identifier}')
        else:
            infant_appointment = Appointment.objects.filter(
                timepoint__lte=180,
                appt_status=IN_PROGRESS_APPT,
                subject_identifier=infant_reg_subject.subject_identifier).order_by('-timepoint').first()
            try:
                infant_visit = InfantVisit.objects.get(
                    appointment=infant_appointment)
            except InfantVisit.DoesNotExist:
                pass
            else:
                infant_visit.save()
