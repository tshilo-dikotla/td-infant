from django import forms
from edc_constants.constants import YES, NO

from td_infant_validators.form_validators import InfantFuNewMedFormValidator
from td_infant_validators.form_validators import InfantFuNewMedItemsFormValidator

from ..models import InfantFuNewMed, InfantFuNewMedItems
from .infant_form_mixin import InfantModelFormMixin


class InfantFuNewMedForm(InfantModelFormMixin):

    form_validator_cls = InfantFuNewMedFormValidator

    def clean(self):
        condition = self.cleaned_data.get('new_medications')
        total_med = self.data.get('infantfunewmeditems_set-TOTAL_FORMS')
        medication = self.data.get('infantfunewmeditems_set-0-medication')
        if condition == YES and int(total_med) < 1:
            raise forms.ValidationError({
                'new_medications': 'Please fill up in-line form'
            })
        elif (condition == NO and medication):
            raise forms.ValidationError({
                'new_medications': "Infant did'nt receive any medication "
                "Please do not fill the table below"
            })

    class Meta:
        model = InfantFuNewMed
        fields = '__all__'


class InfantFuNewMedItemsForm(InfantModelFormMixin):

    form_validator_cls = InfantFuNewMedItemsFormValidator

    class Meta:
        model = InfantFuNewMedItems
        fields = '__all__'
