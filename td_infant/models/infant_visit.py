from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.choices import YES_NO
from edc_constants.constants import ALIVE
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin

from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.model_mixins import CaretakerFieldsMixin
from edc_visit_tracking.model_mixins import VisitModelMixin

from ..choices import ALIVE_DEAD_UNKNOWN, VISIT_INFO_SOURCE
from ..choices import INFANT_VISIT_STUDY_STATUS, VISIT_REASON, INFO_PROVIDER
from .infant_appointment import Appointment


class InfantVisit(
        VisitModelMixin, CreatesMetadataModelMixin,
        ReferenceModelMixin, RequiresConsentFieldsModelMixin,
        CaretakerFieldsMixin, SiteModelMixin, BaseUuidModel):

    """ A model completed by the user on the infant visits. """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    reason = models.CharField(
        verbose_name='Reason for visit',
        max_length=25,
        choices=VISIT_REASON)

    reason_missed = models.CharField(
        verbose_name=(
            'If \'missed\' above, reason scheduled '
            'scheduled visit was missed'),
        blank=True,
        null=True,
        max_length=250)

    covid_visit = models.CharField(
        verbose_name=('Is this a telephonic visit that is occurring '
                      'during COVID-19?'),
        max_length=3,
        choices=YES_NO)

    information_provider = models.CharField(
        verbose_name=(
            'Please indicate who provided most of the information for this infant\'s visit'),
        max_length=20,
        choices=INFO_PROVIDER)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'missed\' above, reason scheduled '
            'scheduled visit was missed'),
        blank=True,
        null=True,
        max_length=25)

    study_status = models.CharField(
        verbose_name="What is the participant's current study status",
        max_length=50,
        choices=INFANT_VISIT_STUDY_STATUS)

    survival_status = models.CharField(
        max_length=10,
        verbose_name='Participant\'s survival status',
        choices=ALIVE_DEAD_UNKNOWN,
        null=True,
        default=ALIVE)

    info_source = models.CharField(
        verbose_name='Source of information?',
        max_length=25,
        choices=VISIT_INFO_SOURCE)

    @property
    def action_item_reason(self):
        return self.study_status

    def get_visit_reason_choices(self):
        return VISIT_REASON

    class Meta(VisitModelMixin.Meta):
        app_label = 'td_infant'
        verbose_name = "Infant Visit"
        verbose_name_plural = "Infant Visit"
