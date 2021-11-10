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

    image = models.FileField(upload_to='infant_notes/')

    user_uploaded = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='user uploaded',)

    datetime_captured = models.DateTimeField(
        default=get_utcnow)

    def clinician_notes_image(self):
        return mark_safe(
            '<embed src="%(url)s" style="border:none" height="100" width="150"'
            'title="clinician notes"></embed>' % {'url': self.image.url})

    clinician_notes_image.short_description = 'Clinician Notes Image'
    clinician_notes_image.allow_tags = True
