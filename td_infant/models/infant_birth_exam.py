from django.db import models
from edc_constants.choices import NORMAL_ABNORMAL, YES_NO_NOT_EVALUATED_NA, NORMAL_ABNORMAL_NOEXAM
from edc_constants.constants import NOT_APPLICABLE

from .infant_crf_model import InfantCrfModel


class InfantBirthExam(InfantCrfModel):

    """ A model completed by the user to record details of the infant's birth. """

    general_activity = models.CharField(
        max_length=15,
        choices=NORMAL_ABNORMAL,
        verbose_name="General Activity? ",
        help_text="Report general activity ON THE DAY of the exam.")

    abnormal_activity = models.CharField(
        verbose_name="If abnormal (specify)",
        max_length=100,
        blank=True,
        null=True)

    physical_exam_result = models.CharField(
        max_length=15,
        choices=NORMAL_ABNORMAL_NOEXAM,
        verbose_name="What was the result of the Physical Exam? ",
        help_text="")

    heent_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was HEENT Exam Normal? ",
        default=NOT_APPLICABLE,
        help_text="")

    heent_no_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True)

    resp_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Respiratory Exam Normal?",
        default=NOT_APPLICABLE,
        help_text="")

    resp_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True)

    cardiac_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Cardiac Exam Normal?",
        default=NOT_APPLICABLE,
        help_text="")

    cardiac_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated,(specify)",
        blank=True,
        null=True)

    abdominal_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        default=NOT_APPLICABLE,
        verbose_name="Was Abdominal Exam Normal?",
        help_text="")

    abdominal_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True)

    skin_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Skin Exam Normal?",
        help_text="",
        default=NOT_APPLICABLE,)

    skin_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        help_text="",
        blank=True,
        null=True)

    neurologic_exam = models.CharField(
        max_length=15,
        choices=YES_NO_NOT_EVALUATED_NA,
        verbose_name="Was Neurological Exam Normal?",
        default=NOT_APPLICABLE,
        help_text="")

    neuro_exam_other = models.TextField(
        verbose_name="If abnormal or not evaluated, specify",
        blank=True,
        null=True)

    other_exam_info = models.TextField(
        max_length=250,
        verbose_name="Other infant exam information",
        blank=True,
        null=True)

    class Meta(InfantCrfModel.Meta):
        app_label = 'td_infant'
        verbose_name = "Infant Birth: Exam"
        verbose_name_plural = "Infant Birth: Exam"
