from td_infant_validators.form_validators import InfantFuFormValidator

from ..models import InfantFu
from .infant_form_mixin import InfantModelFormMixin


class InfantFuForm(InfantModelFormMixin):

    form_validator_cls = InfantFuFormValidator

    def clean(self):
        super().clean()

    class Meta:
        model = InfantFu
        fields = '__all__'
