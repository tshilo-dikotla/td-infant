from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFuDx, InfantFuDxItems

from td_infant_validators.form_validators import InfantFuDxItemsFormValidator


class InfantFuDxForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuDx
        fields = '__all__'


class InfantFuDxItemsForm(InfantModelFormMixin):

    form_validator_cls = InfantFuDxItemsFormValidator

    class Meta:
        model = InfantFuDxItems
        fields = '__all__'
