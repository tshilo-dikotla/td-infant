from django import forms
from edc_constants.constants import YES
from td_infant_validators.form_validators import InfantFuNewMedFormValidator
from td_infant_validators.form_validators import InfantFuNewMedItemsFormValidator

from ..models import InfantFuNewMed, InfantFuNewMedItems
from .infant_form_mixin import InfantModelFormMixin


class InfantFuNewMedForm(InfantModelFormMixin):

    form_validator_cls = InfantFuNewMedFormValidator

    def clean(self):
        super().clean()
        condition = self.cleaned_data.get('new_medications')
        total_med = self.data.get('infantfunewmeditems_set-TOTAL_FORMS')
        if condition == YES and int(total_med) < 1:
            raise forms.ValidationError({
                'new_medications': 'Please fill up in-line form'
            })

    class Meta:
        model = InfantFuNewMed
        fields = '__all__'


class InfantFuNewMedItemsForm(InfantModelFormMixin):

    form_validator_cls = InfantFuNewMedItemsFormValidator

    class Meta:
        model = InfantFuNewMedItems
        fields = '__all__'
