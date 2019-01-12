from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFuNewMed, InfantFuNewMedItems
from td_infant_validators.form_validators import InfantFuNewMedItemsFormValidator


class InfantFuNewMedForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuNewMed
        fields = '__all__'


class InfantFuNewMedItemsForm(InfantModelFormMixin):

    form_validator_cls = InfantFuNewMedItemsFormValidator

    class Meta:
        model = InfantFuNewMedItems
        fields = '__all__'
