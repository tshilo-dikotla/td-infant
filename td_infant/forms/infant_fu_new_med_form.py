from td_infant_validators.form_validators import InfantFuNewMedFormValidator
from td_infant_validators.form_validators import InfantFuNewMedItemsFormValidator

from ..models import InfantFuNewMed, InfantFuNewMedItems
from .infant_form_mixin import InfantModelFormMixin


class InfantFuNewMedForm(InfantModelFormMixin):

    form_validator_cls = InfantFuNewMedFormValidator

    def clean(self):
        cleaned_data = super().clean()
        arv_count = int(self.data.get('infantfunewmeditems_set-TOTAL_FORMS'))
        return cleaned_data

    class Meta:
        model = InfantFuNewMed
        fields = '__all__'


class InfantFuNewMedItemsForm(InfantModelFormMixin):

    form_validator_cls = InfantFuNewMedItemsFormValidator

    class Meta:
        model = InfantFuNewMedItems
        fields = '__all__'
