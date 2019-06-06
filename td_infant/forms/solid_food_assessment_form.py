from td_infant_validators.form_validators import SolidFoodAssessementFormValidator
from django.apps import apps as django_apps

from ..models import SolidFoodAssessment
from .infant_form_mixin import InfantModelFormMixin


class SolidFoodAssessmentForm(InfantModelFormMixin):

    form_validator_cls = SolidFoodAssessementFormValidator

    infant_birth = 'td_infant.infantbirth'

    def clean(self):
        super().clean()

    def save(self, commit=True):
        instance = super(SolidFoodAssessmentForm, self).save(commit=False)
        age_solid_food = self.cleaned_data.get('age_solid_food')
        if not age_solid_food:
            birth_date = self.infant_birth_cls.objects.get(
                subject_identifier=self.cleaned_data.get(
                    'infant_visit').subject_identifier).dob
            report_date = self.cleaned_data.get('report_datetime').date()
            date_diff = (report_date - birth_date).days
            weeks = date_diff / 7
            months = weeks / 4
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
