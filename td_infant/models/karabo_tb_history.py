from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO_DONT_KNOW, YES_NO
from edc_constants.constants import NO

from .infant_crf_model_mixin import InfantCrfModelMixin

from .list_models import (
    CoughingRelation, WeightLossRelation, NightSweatsRelation,
    DiagnosisRelation, FeverRelation)


class KaraboTuberculosisHistory(InfantCrfModelMixin):
    """
    crf model about tuberculosis treatment history in family
    members relating to the infant
    """

    coughing = models.CharField(
        verbose_name=(
            'Since the last scheduled visit, or if this is the enrollment '
            'visit, since birth, has any member of '
            'the household where your infant stayed been '
            'coughing for two weeks or more?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    coughing_rel = models.ManyToManyField(
        CoughingRelation,
        verbose_name=(
            'If yes to question 3, please indicate the '
            'relationship of this individual or individuals to your infant.'
        )
    )

    other_coughing_rel = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    fever = models.CharField(
        verbose_name=(
            'Since the last scheduled visit, or if this is the enrollment '
            'visit, since birth, has any member of the household where '
            'your infant stayed had an unexplained'
            ' fever concerning for tuberculosis?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    fever_rel = models.ManyToManyField(
        FeverRelation,
        verbose_name=(
            'If yes to question 6, please indicate the relationship'
            ' of the person or persons to the infant'),
    )

    other_fever_rel = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    weight_loss = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit, or if this is the '
            'enrollment visit, since birth, has any member'
            ' of the household where your infant stayed had any unexplained'
            ' weight loss?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    weight_loss_rel = models.ManyToManyField(
        WeightLossRelation,
        verbose_name=(
            'If yes to question 9, please indicate the relationship'
            ' of the person or persons to the infant.'),
    )

    other_weight_loss = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    night_sweats = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit, or if this is the '
            'enrollment visit, since birth, has any member'
            ' of the household where your infant stayed had night sweats?'
            ' An adult or child would be considered to have night sweats'
            ' if they have had more than two nights of waking up with '
            'their night clothing drenched due to sweating with a need to'
            ' change the night clothing.'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    night_sweats_rel = models.ManyToManyField(
        NightSweatsRelation,
        verbose_name=(
            'If yes to question 12, please indicate the relationship of the '
            'person or persons to the infant'),
    )

    other_night_sweats = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    diagnosis = models.CharField(
        verbose_name=(
            'Since the last scheduled visit, or if this is the '
            'enrollment visit, since birth, has any member of the household'
            ' where your infant has stayed been diagnosed with tuberculosis?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    diagnosis_rel = models.ManyToManyField(
        DiagnosisRelation,
        verbose_name=(
            'If yes to question 15, please indicate the relationship of'
            ' the person or persons to the infant'),
    )

    other_diagnosis_rel = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    tb_exposure = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit, or if this is the '
            'enrollment visit, since birth, do you have any reason'
            ' to suspect your infant was exposed to tuberculosis outside of'
            ' the household.'),
        help_text=('e.g: public transport, health facility visit, church or '
                   'community gathering.'),
        max_length=15,
        choices=YES_NO_DONT_KNOW
    )

    tb_exposure_det = models.TextField(
        verbose_name=(
            'If yes to question 18, please comment on the nature'
            ' of the exposure'),
        max_length=255,
        help_text='please comment on the nature of the exposure',
        null=True,
        blank=True
    )

    put_offstudy = models.CharField(
        verbose_name=(
            'Is the participant going offstudy?'),
        max_length=3,
        choices=YES_NO,
        default=NO,
        help_text='Select YES only if the participant is going off study.',
    )

    class Meta:
        app_label = 'td_infant'
        verbose_name = "Karabo Tuberculosis History"
        verbose_name_plural = "Karabo Tuberculosis History"
