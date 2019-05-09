import datetime
from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from td_infant_validators.form_validators import (
    InfantBirthFeedingFormValidator)

from ..models import InfantBirthFeedingVaccine
from .infant_form_mixin import InfantModelFormMixin


class InfantBirthFeedinVaccineForm(InfantModelFormMixin):

    form_validator_cls = InfantBirthFeedingFormValidator
    infant_birth_model = 'td_infant.infantbirth'

    @property
    def infant_birth_cls(self):
        return django_apps.get_model(self.infant_birth_model)

    def validate_against_birth_date(self, infant_identifier=None,
                                    vaccine_date=None):

        try:
            infant_birth = self.infant_birth_cls.objects.get(
                subject_identifier=infant_identifier)
        except self.infant_birth_cls.DoesNotExist:

            raise ValidationError(
                'Please complete Infant Birth form '
                f'before  proceeding.')
        else:
            infant_date = infant_birth.report_datetime.date()
            if vaccine_date and infant_date:
                if vaccine_date < infant_date:
                    raise forms.ValidationError(
                        "The date vaccine was given should not be before the "
                        f"delivery date Got {vaccine_date} "
                        f"delivery date {infant_date}"
                    )

    def clean(self):
        cleaned_data = super().clean()
        self.validate_vaccine_date_against_birth_date()
        return cleaned_data

    def validate_vaccine_date_against_birth_date(self):
        infant_identifier = self.cleaned_data.get(
            'infant_visit').subject_identifier
        total = self.data.get('infantvaccines_set-TOTAL_FORMS')
        for i in range(int(total)):
            vaccine_date = self.data.get(
                'infantvaccines_set-' + str(i) + '-vaccine_date')
            if vaccine_date:
                vaccine_date = datetime.datetime.strptime(vaccine_date,
                                                      '%Y-%m-%d')
                self.validate_against_birth_date(infant_identifier,
                                             vaccine_date.date())

    class Meta:
        model = InfantBirthFeedingVaccine
        fields = '__all__'
