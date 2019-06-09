from td_infant_validators.form_validators import (
    InfantNvpAdjustmentFormValidator)

from ..models import InfantNvpAdjustment
from .infant_form_mixin import InfantModelFormMixin


class InfantNvpAdjustmentForm(InfantModelFormMixin):

    form_validator_cls = InfantNvpAdjustmentFormValidator

    def clean(self):
        super().clean()

    class Meta:
        model = InfantNvpAdjustment
        fields = '__all__'
