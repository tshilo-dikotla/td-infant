from td_infant_validators.form_validators import InfantFuDxFormValidator
from td_infant_validators.form_validators import InfantFuDxItemsFormValidator

from ..models import InfantFuDx, InfantFuDxItems
from .infant_form_mixin import InfantModelFormMixin


class InfantFuDxForm(InfantModelFormMixin):

    form_validator_cls = InfantFuDxFormValidator

    class Meta:
        model = InfantFuDx
        fields = '__all__'


class InfantFuDxItemsForm(InfantModelFormMixin):

    form_validator_cls = InfantFuDxItemsFormValidator

    class Meta:
        model = InfantFuDxItems
        fields = '__all__'
