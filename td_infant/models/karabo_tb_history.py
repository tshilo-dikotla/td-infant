from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO_DONT_KNOW, YES_NO
from edc_constants.constants import NO

from ..choices import FAMILY_RELATION
from .infant_crf_model_mixin import InfantCrfModelMixin


class KaraboTuberculosisHistory(InfantCrfModelMixin):
    """
    crf model about tuberculosis treatment history in family
    members relating to the infant
    """

    coughing = models.CharField(
        verbose_name=(
            'Since the last scheduled visit or if this is the enrollment '
            'visit, since birth, has any member of '
            'the household where your has infant stayed been '
            'coughing for two weeks or more?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    coughing_rel = models.CharField(
        verbose_name=(
            'If yes to question 2, please indicate the '
            'relationship of this individual or individuals to your infant.'
        ),
        max_length=25,
        choices=FAMILY_RELATION
    )

    other_coughing_rel = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    fever = models.CharField(
        verbose_name=(
            'Since the last scheduled visit or if this is the enrollment '
            'visit, since birth, has any member of the household where '
            'your infant stayed had an unexplained'
            ' fever concerning for tuberculosis?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    fever_rel = models.CharField(
        verbose_name=(
            'If yes to question 5, please indicate the relationship'
            ' of the person or persons to the infant'),
        max_length=25,
        choices=FAMILY_RELATION
    )

    other_fever_rel = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    weight_loss = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit or if this is the '
            'enrollment visit, since birth, has any member'
            ' of the household where your infant stayed had any unexplained'
            ' weight loss?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    weight_loss_rel = models.CharField(
        verbose_name=(
            'If yes to question 8, please indicate the relationship'
            ' of the person or persons to the infant.'),
        max_length=25,
        choices=FAMILY_RELATION
    )

    other_weight_loss = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    night_sweats = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit or if this is the '
            'enrollment visit, since birth, has any member'
            ' of the household where your infant stayed had night sweats?'
            ' An adult or child would be considered to have night sweats'
            ' if they have had more than two nights of walking up with '
            'their night clothing drenched due to sweating with a need to'
            ' change the night clothing.'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    night_sweats_rel = models.CharField(
        verbose_name=(
            'If yes to question 11, please indicate the relationship of the '
            'person or persons to the infant'),
        max_length=25,
        choices=FAMILY_RELATION
    )

    other_night_sweats = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    diagnosis = models.CharField(
        verbose_name=(
            'Since the last scheduled visit or if this is the '
            'enrollment visit, since birth, has any member of the household'
            ' where your infant has stayed been diagnosed with tuberculosis?'),
        max_length=12,
        choices=YES_NO_DONT_KNOW
    )

    diagnosis_rel = models.CharField(
        verbose_name=(
            'If yes to question 14, please indicate the relationship of'
            ' the person or persons to the infant'),
        max_length=25,
        choices=FAMILY_RELATION
    )

    other_diagnosis_rel = OtherCharField(
        max_length=35,
        help_text='Indicate Relationship',
        null=True,
        blank=True
    )

    tb_exposure = models.CharField(
        verbose_name=(
            'Since the last attended scheduled visit or if this is the '
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
            'If yes to question 16, please comment on the nature'
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
        verbose_name_plural = "Karabo Tuberculosis Histories"
