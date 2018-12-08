from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFuDx, InfantFuDxItems


class InfantFuDxForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuDx
        fields = '__all__'


class InfantFuDxItemsForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuDxItems
        fields = '__all__'
