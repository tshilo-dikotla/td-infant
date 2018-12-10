from django.db import models
from edc_appointment.models import Appointment
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.constants import (DEAD, MALE)
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.choices import VISIT_REASON_MISSED
from edc_visit_tracking.constants import (
    UNSCHEDULED, SCHEDULED, COMPLETED_PROTOCOL_VISIT, MISSED_VISIT)
from edc_visit_tracking.constants import LOST_VISIT
from edc_visit_tracking.model_mixins import CaretakerFieldsMixin
from edc_visit_tracking.model_mixins import VisitModelMixin

from ..choices import VISIT_REASON
from .infant_birth import InfantBirth


class InfantVisit(CaretakerFieldsMixin, VisitModelMixin,
                  ReferenceModelMixin, CreatesMetadataModelMixin,
                  SiteModelMixin, RequiresConsentFieldsModelMixin, BaseUuidModel):

    """ A model completed by the user on the infant visits. """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    def requires_circumcision_for_male_at_2030_or_2060(self):
        infant_birth = InfantBirth.objects.get(
            registered_subject=self.appointment.registered_subject)
        if infant_birth.gender == MALE:
            if self.appointment.visit_definition.code == '2030':
                self.crf_is_required(
                    self.appointment, 'td_infant', 'infantcircumcision')
            if self.appointment.visit_definition.code == '2060':
                appointment = Appointment.objects.get(
                    visit_definition__code='2030',
                    registered_subject=self.appointment.registered_subject)
                if appointment:
                    infant_visit = InfantVisit.objects.get(
                        appointment=appointment)
                    if infant_visit.reason == MISSED_VISIT:
                        self.crf_is_required(
                            self.appointment, 'td_infant', 'infantcircumcision')

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def get_visit_reason_no_follow_up_choices(self):
        """Returns the visit reasons that do not imply any data collection;
        that is, the subject is not available."""
        dct = {}
        for item in VISIT_REASON_MISSED:
            if item not in [COMPLETED_PROTOCOL_VISIT, LOST_VISIT]:
                dct.update({item: item})
        return dct

    class Meta(VisitModelMixin.Meta):
        verbose_name = "Infant Visit"
        verbose_name_plural = "Infant Visit"
