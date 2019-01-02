from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InfantBirth


class InfantBirthForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = InfantBirth
        fields = '__all__'
