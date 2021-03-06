from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO
from edc_visit_tracking.model_mixins import CrfInlineModelMixin

from ..choices import ARV_MODIFICATION_REASON, ARV_DRUG_LIST, DOSE_STATUS, ARV_STATUS

from .infant_crf_model_mixin import InfantCrfModelMixin


class InfantArvProph(InfantCrfModelMixin):
    """ A model completed by the user on the infant's nvp or azt prophylaxis. """

    prophylatic_nvp = models.CharField(
        verbose_name=(
            'Was the baby supposed to be taking taking prophylactic'
            ' antiretroviral medication for '
            'any period since the last attended scheduled visit?'),
        max_length=3,
        choices=YES_NO)

    arv_status = models.CharField(
        max_length=25,
        verbose_name=(
            "What is the status of the participant's ARV prophylaxis at"
            " this visit or since the last visit? "),
        choices=ARV_STATUS,
        help_text="referring to prophylaxis other than single dose NVP")

    class Meta(InfantCrfModelMixin.Meta):
        verbose_name = 'Infant NVP or AZT Proph'
        verbose_name_plural = 'Infant NVP or AZT Proph'


class InfantArvProphMod(CrfInlineModelMixin, BaseUuidModel):
    """ A model completed by the user on the infant's nvp or azt prophylaxis modifications. """

    infant_arv_proph = models.ForeignKey(
        InfantArvProph, on_delete=models.CASCADE)

    arv_code = models.CharField(
        verbose_name="ARV Code",
        max_length=30,
        choices=ARV_DRUG_LIST,
    )

    dose_status = models.CharField(
        max_length=25,
        choices=DOSE_STATUS,
        verbose_name="Dose Status",
    )

    modification_date = models.DateField(
        verbose_name="Date ARV Modified",
    )

    modification_code = models.CharField(
        max_length=50,
        choices=ARV_MODIFICATION_REASON,
        verbose_name="Reason for Modification",
    )

    other_reason = models.CharField(
        verbose_name="Specify Other",
        max_length=100,
        null=True,
        blank=True)

    def natural_key(self):
        return (self.arv_code,) + self.infant_arv_proph.natural_key()

    class Meta:
        verbose_name = 'Infant NVP or AZT Proph: Mods'
        verbose_name_plural = 'Infant NVP or AZT Proph: Mods'
        unique_together = (
            'infant_arv_proph', 'arv_code', 'dose_status', 'modification_date')
