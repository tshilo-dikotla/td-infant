from django.db import models
from django.utils.html import mark_safe
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from .infant_crf_model_mixin import InfantCrfModelMixin


class InfantClinicianNotes(InfantCrfModelMixin):

    class Meta(InfantCrfModelMixin.Meta):
        app_label = 'td_infant'
        verbose_name = 'Infant Clinician Notes'
        verbose_name_plural = 'Infant Clinician Notes'


class ClinicianNotesImage(BaseUuidModel):

    clinician_notes = models.ForeignKey(
        InfantClinicianNotes,
        on_delete=models.PROTECT,
        related_name='infant_clinician_notes',)
    image = models.ImageField(upload_to='media/')
    user_uploaded = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='user uploaded',)
    datetime_captured = models.DateTimeField(
        default=get_utcnow)

    def clinician_notes_image(self):
        return mark_safe(
            '<a href="%(url)s">'
            '<img src="%(url)s" style="padding-right:150px" width="150" height="100" />'
            '</a>' % {'url': self.image.url})

    clinician_notes_image.short_description = 'Clinician Notes Image'
    clinician_notes_image.allow_tags = True
