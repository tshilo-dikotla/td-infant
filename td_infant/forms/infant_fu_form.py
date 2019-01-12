from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFu

from td_infant_validators.form_validators import InfantFuFormValidator


class InfantFuForm(InfantModelFormMixin):

    form_validator_cls = InfantFuFormValidator

    class Meta:
        model = InfantFu
        fields = '__all__'
