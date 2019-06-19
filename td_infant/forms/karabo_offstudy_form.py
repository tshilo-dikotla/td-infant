from django import forms

from td_infant_validators.form_validators import KaraboOffstudyFormValidator

from ..models import KaraboOffstudy
from .infant_form_mixin import InfantModelFormMixin


class KaraboOffstudyForm(InfantModelFormMixin, forms.ModelForm):

    form_validator_cls = KaraboOffstudyFormValidator

    class Meta:
        model = KaraboOffstudy
        fields = '__all__'
