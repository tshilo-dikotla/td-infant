from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO
#from edc_sync.models import SyncModelMixin, SyncHistoricalRecords
from edc_visit_tracking.model_mixins import CrfInlineModelMixin

from ..choices import MEDICATIONS, DRUG_ROUTE

# from ..managers import InfantFuNewMedItemsManager

from .infant_crf_model import InfantCrfModel


class InfantFuNewMed(InfantCrfModel):

    """ A model completed by the user on the infant's follow up medications. """

    new_medications = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Has the child recieved a NEW course of any of the following medications "
                     "since the last attended scheduled visit",
        help_text="do not report if the same course was recorded at previous visit. "
                  "only report oral and intravenous meds",
    )

    class Meta(InfantCrfModel.Meta):
        app_label = 'td_infant'
        verbose_name = "Infant FollowUp: New Medication"
        verbose_name_plural = "Infant FollowUp: New Medication"


class InfantFuNewMedItems(CrfInlineModelMixin, BaseUuidModel):

    """A model completed by the user on the infant's follow up medication items."""

    infant_fu_med = models.ForeignKey(InfantFuNewMed, on_delete=models.CASCADE)

    medication = models.CharField(
        max_length=100,
        choices=MEDICATIONS,
        verbose_name="Medication",
    )

    other_medication = OtherCharField()

    date_first_medication = models.DateField(
        verbose_name="Date of first medication use",
    )

    stop_date = models.DateField(
        verbose_name="Date medication was stopped",
        blank=True,
        null=True,
    )

    drug_route = models.CharField(
        max_length=20,
        choices=DRUG_ROUTE,
        verbose_name="Drug route",
    )

#     objects = InfantFuNewMedItemsManager()

    def natural_key(self):
        return (self.medication, ) + self.infant_fu_med.natural_key()

    class Meta(InfantCrfModel.Meta):
        verbose_name = "Infant FollowUp: New Med Items"
        verbose_name_plural = "Infant FollowUp: New Med Items"
