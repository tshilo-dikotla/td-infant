from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin


class OnScheduleInfantBirth(OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by infant birth.
    """
    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def put_on_schedule(self):
        pass

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(OnScheduleInfantBirth, self).save(*args, **kwargs)

    def get_consent_version(self):
        subject_consent_cls = django_apps.get_model(
            'td_infant.infantdummysubjectconsent')
        try:
            subject_consent_obj = subject_consent_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except subject_consent_cls.DoesNotExist:
            raise ValidationError(
                'Missing Infant Dummy Consent form. Cannot proceed.')
        else:
            return subject_consent_obj.version
