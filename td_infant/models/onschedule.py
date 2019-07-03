from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin


class OnScheduleInfantBirth(OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by infant birth.
    """

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    schedule_name = models.CharField(max_length=25,
                                     blank=True,
                                     null=True)

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
        subject_consent_objs = subject_consent_cls.objects.filter(
            subject_identifier=self.subject_identifier).order_by(
                '-consent_datetime')
        if subject_consent_objs:
            return subject_consent_objs.first().version
        else:
            raise ValidationError(
                'Missing Infant Dummy Consent form. Cannot proceed.')

    class Meta:
        unique_together = ('subject_identifier', 'schedule_name')
