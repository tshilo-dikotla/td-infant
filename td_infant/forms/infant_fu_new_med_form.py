from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFuNewMed, InfantFuNewMedItems


class InfantFuNewMedForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuNewMed
        fields = '__all__'


class InfantFuNewMedItemsForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuNewMedItems
        fields = '__all__'
