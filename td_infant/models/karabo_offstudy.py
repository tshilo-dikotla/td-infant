from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import date_not_before_study_start
from edc_protocol.validators import datetime_not_before_study_start

from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from ..choices import KARABO_OFF_STUDY_REASON
from .infant_crf_model_mixin import InfantCrfModelMixin


class KaraboOffstudy(InfantCrfModelMixin):

    """ A model completed by the user when the infant is taken off study. """

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    offschedule_datetime = models.DateTimeField(
        verbose_name="Date and time subject taken off schedule",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow)

    reason = models.CharField(
        verbose_name=('Please code the primary reason participant taken'
                      ' off-study'),
        max_length=115,
        choices=KARABO_OFF_STUDY_REASON)

    offstudy_date = models.DateField(
        verbose_name="Off-study Date",
        validators=[
            date_not_before_study_start,
            date_not_future])

    reason_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment",
        blank=True,
        null=True)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def take_off_schedule(self):
        pass

    def get_consent_version(self):
        subject_consent_cls = django_apps.get_model(
            'td_infant.infantdummysubjectconsent')
        subject_consent_objs = subject_consent_cls.objects.filter(
            subject_identifier=self.infant_visit.subject_identifier).order_by(
                '-consent_datetime')
        if subject_consent_objs:
            return subject_consent_objs.first().version
        else:
            raise ValidationError(
                'Missing Infant Dummy Consent form. Cannot proceed.')

    def save(self, *args, **kwargs):
        self.report_datetime = self.offschedule_datetime
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'td_infant'
        verbose_name = "Karabo Off-Study"
        verbose_name_plural = "Karabo Off-Study"
