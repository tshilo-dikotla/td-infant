from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future

from edc_visit_tracking.model_mixins import CrfInlineModelMixin

from ..choices import (
    IMMUNIZATIONS, INFANT_AGE_VACCINE_GIVEN, REASONS_VACCINES_MISSED)
from ..choices import YES_NO_UNKNOWN
from .infant_crf_model_mixin import InfantCrfModelMixin


class InfantFuImmunizations(InfantCrfModelMixin):

    """ A model completed by the user on the infant's follow up immunizations. """

    vaccines_received = models.CharField(
        max_length=25,
        choices=YES_NO_UNKNOWN,
        verbose_name="Did this infant receive any vaccinations since the last visit",
        help_text="")

    vaccines_missed = models.CharField(
        max_length=25,
        choices=YES_NO_UNKNOWN,
        verbose_name="Is the child missing any vaccinations?",
        help_text="")

    class Meta(InfantCrfModelMixin.Meta):
        app_label = 'td_infant'
        verbose_name = "Infant FollowUp: Immunizations"
        verbose_name_plural = "Infant FollowUp: Immunizations"


class VaccinesReceived(CrfInlineModelMixin, BaseUuidModel):

    """ALL possible vaccines given to infant"""

    infant_fu_immunizations = models.ForeignKey(
        InfantFuImmunizations, on_delete=models.CASCADE)

    received_vaccine_name = models.CharField(
        verbose_name="Received vaccine name",
        choices=IMMUNIZATIONS,
        max_length=100,
        null=True,
        blank=True)

    date_given = models.DateField(
        verbose_name="Date Given",
        validators=[
            date_not_future, ],
        null=True,
        blank=True)

    infant_age = models.CharField(
        verbose_name="Infant age when vaccine given",
        choices=INFANT_AGE_VACCINE_GIVEN,
        null=True,
        blank=True,
        max_length=35)

    def natural_key(self):
        return (self.received_vaccine_name,) + self.infant_fu_immunizations.natural_key()

    class Meta:
        app_label = 'td_infant'
        verbose_name = 'Received Vaccines'
        verbose_name_plural = 'Received Vaccines'
        unique_together = (
            'received_vaccine_name', 'infant_fu_immunizations', 'infant_age')


class VaccinesMissed(CrfInlineModelMixin, BaseUuidModel):

    """ALL vaccines missed by infant"""

    parent_model_attr = 'infant_fu_immunizations'

    infant_fu_immunizations = models.ForeignKey(
        InfantFuImmunizations, on_delete=models.CASCADE)

    missed_vaccine_name = models.CharField(
        verbose_name="Missed vaccine name",
        choices=IMMUNIZATIONS,
        max_length=100,
        null=True,
        blank=True)

    reason_missed = models.CharField(
        verbose_name="Reasons infant missed vaccines",
        choices=REASONS_VACCINES_MISSED,
        max_length=100,
        null=True,
        blank=True)

    reason_missed_other = OtherCharField()

    def natural_key(self):
        return (self.missed_vaccine_name,) + self.infant_fu_immunizations.natural_key()

    class Meta:
        app_label = 'td_infant'
        verbose_name = 'Missed Vaccines'
        verbose_name_plural = 'Missed Vaccines'
        unique_together = (
            'missed_vaccine_name', 'infant_fu_immunizations', 'reason_missed')
