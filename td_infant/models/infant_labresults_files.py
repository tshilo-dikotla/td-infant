from django.db import models
from django.utils.html import mark_safe
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from .infant_crf_model_mixin import InfantCrfModelMixin


class InfantLabResultsFiles(InfantCrfModelMixin):

    class Meta(InfantCrfModelMixin.Meta):
        app_label = 'td_infant'
        verbose_name = 'Infant Lab Results Files'
        verbose_name_plural = 'Infant Lab Results Files'


class LabResultsFile(BaseUuidModel):

    lab_results = models.ForeignKey(
        InfantLabResultsFiles,
        on_delete=models.PROTECT,
        related_name='infant_lab_results',)

    image = models.FileField(upload_to='infant_lab_results/')

    user_uploaded = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='user uploaded',)

    datetime_captured = models.DateTimeField(
        default=get_utcnow)

    def lab_results_preview(self):
        return mark_safe(
            '<embed src="%(url)s" style="border:none" height="100" width="150"'
            'title="Lab results"></embed>' % {'url': self.image.url})

    lab_results_preview.short_description = 'Preview'
    lab_results_preview.allow_tags = True
