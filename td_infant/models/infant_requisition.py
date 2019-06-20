from decimal import Decimal

from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_lab.choices import PRIORITY
from edc_lab.models import RequisitionIdentifierMixin
from edc_lab.models import RequisitionModelMixin, RequisitionStatusMixin
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_reference.model_mixins import RequisitionReferenceModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as VisitTrackingCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from ..choices import STUDY_SITES, ITEM_TYPE, VOLUME_UNITS
from .infant_visit import InfantVisit
from .search_slug_model_mixin import SearchSlugModelMixin


class Manager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass


class InfantRequisition(
        NonUniqueSubjectIdentifierFieldMixin,
        RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin,
        VisitTrackingCrfModelMixin, SubjectScheduleCrfModelMixin,
        RequiresConsentFieldsModelMixin, PreviousVisitModelMixin,
        RequisitionReferenceModelMixin, UpdatesRequisitionMetadataModelMixin,
        SearchSlugModelMixin, BaseUuidModel):

    lab_profile_name = 'td_infant'

    infant_visit = models.ForeignKey(InfantVisit, on_delete=PROTECT)

    estimated_volume = models.DecimalField(
        verbose_name='Estimated Volume',
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(0.01))],
        null=True,
        blank=True,
        help_text=(
            'If applicable, estimated volume of sample for this test/order. '
            'This is the total volume if number of "tubes" above is greater than 1'))

    volume_units = models.CharField(
        verbose_name='Volume Units',
        max_length=5,
        choices=VOLUME_UNITS,
        blank=True
        )

    study_site = models.CharField(
        verbose_name='Study site',
        max_length=25,
        choices=STUDY_SITES,
        default=settings.DEFAULT_STUDY_SITE)

    priority = models.CharField(
        verbose_name='Priority',
        max_length=25,
        choices=PRIORITY,
        default='normal',)

    item_type = models.CharField(
        verbose_name='Item collection type',
        max_length=25,
        choices=ITEM_TYPE,
        default=NOT_APPLICABLE)

    comments = models.TextField(
        max_length=350,
        null=True,
        blank=True)

    objects = Manager()

    history = HistoricalRecords()

    def __str__(self):
        return (
            f'{self.requisition_identifier} '
            f'{self.panel_object.verbose_name}')

    def save(self, *args, **kwargs):
        if not self.id:
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.protocol_number = edc_protocol_app_config.protocol_number
        self.subject_identifier = self.infant_visit.subject_identifier
        self.consent_version = self.get_consent_version()
        super().save(*args, **kwargs)

    def get_consent_version(self):
        infant_consent_cls = django_apps.get_model(
            'td_infant.infantdummysubjectconsent')
        try:
            infant_consent_obj = infant_consent_cls.objects.get(
                subject_identifier=self.infant_visit.subject_identifier)
        except infant_consent_cls.DoesNotExist:
            raise ValidationError(
                'Missing Infant Dummy Consent form.')
        return infant_consent_obj.version

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend([
            'requisition_identifier',
            'human_readable_identifier', 'identifier_prefix'])
        return fields

    class Meta:
        unique_together = ('panel', 'infant_visit')
