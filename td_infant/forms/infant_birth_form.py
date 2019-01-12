from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InfantBirth
from td_infant_validators.form_validators import InfantBirthFormValidator


class InfantBirthForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = InfantBirthFormValidator

    class Meta:
        model = InfantBirth
        fields = '__all__'
