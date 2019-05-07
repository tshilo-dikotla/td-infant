from django.db import models
from edc_base.model_mixins.base_uuid_model import BaseUuidModel

from ..choices import INFANT_VACCINATIONS, FEEDING_CHOICES
from .infant_crf_model_mixin import InfantCrfModelMixin


class InfantBirthFeedingVaccine(InfantCrfModelMixin):

    """ A model completed by the user on the infant's feeding &
    vaccination/ immunization. """

    feeding_after_delivery = models.CharField(
        max_length=50,
        choices=FEEDING_CHOICES,
        verbose_name="How was the infant being fed immediately after delivery? ",
        help_text=" ...before discharge from maternity")

    comments = models.TextField(
        max_length=250,
        verbose_name="Comment if any additional pertinent information: ",
        blank=True,
        null=True)

    class Meta(InfantCrfModelMixin.Meta):
        app_label = 'td_infant'
        verbose_name = "Birth Feeding & Vaccination"


class InfantVaccines(BaseUuidModel):

    infant_birth_feed_vaccine = models.ForeignKey(
        InfantBirthFeedingVaccine, on_delete=models.CASCADE)

    vaccination = models.CharField(
        choices=INFANT_VACCINATIONS,
        verbose_name="Since delivery, did the child receive any of the following vaccinations",
        max_length=100)

    vaccine_date = models.DateField(
        verbose_name='Date Vaccine was given')

    class Meta:
        verbose_name = "Infant Vaccines"
        verbose_name_plural = "Infant Vaccines"
        unique_together = (infant_birth_feed_vaccine, vaccination)
