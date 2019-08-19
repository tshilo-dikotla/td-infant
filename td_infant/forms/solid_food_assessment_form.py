from td_infant_validators.form_validators import CrfOffStudyFormValidator
from td_infant_validators.form_validators import SolidFoodAssessementFormValidator

from django.apps import apps as django_apps

from ..models import SolidFoodAssessment
from .infant_form_mixin import InfantModelFormMixin
from dateutil.relativedelta import relativedelta


class SolidFoodAssessmentForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    form_validator_cls = SolidFoodAssessementFormValidator

    infant_birth = 'td_infant.infantbirth'
    infant_feeding = 'td_infant.infantfeeding'

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    def save(self, commit=True):
        instance = super(SolidFoodAssessmentForm, self).save(commit=False)
        age_solid_food = self.cleaned_data.get('age_solid_food')
        if not age_solid_food:
            birth_date = self.infant_birth_cls.objects.get(
                subject_identifier=self.cleaned_data.get(
                    'infant_visit').subject_identifier).dob
            solids_intro_date = self.infant_feeding_cls.objects.filter(
                infant_visit__subject_identifier=self.cleaned_data.get(
                    'infant_visit').subject_identifier,
                formula_intro_date__isnull=False).last().formula_intro_date
            difference = relativedelta(solids_intro_date, birth_date)
            months = difference.months
            instance.age_solid_food = months
        if commit:
            instance.save()
        return instance

    class Meta:
        model = SolidFoodAssessment
        fields = '__all__'

    @property
    def infant_birth_cls(self):
        return django_apps.get_model(self.infant_birth)

    @property
    def infant_feeding_cls(self):
        return django_apps.get_model(self.infant_feeding)
