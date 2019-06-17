from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_identifier.managers import SubjectIdentifierManager

from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from td_maternal.models.model_mixins import ConsentVersionModelModelMixin


class InfantOffSchedule(ConsentVersionModelModelMixin, OffScheduleModelMixin, BaseUuidModel):

    schedule_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        unique=True)

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def take_off_schedule(self):
        pass

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

    class Meta:
        pass
