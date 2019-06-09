from td_infant_validators.form_validators import InfantNvpDispensingFormValidator

from ..models import InfantNvpDispensing
from .infant_form_mixin import InfantModelFormMixin


class InfantNvpDispensingForm(InfantModelFormMixin):

    form_validator_cls = InfantNvpDispensingFormValidator

    def clean(self):
        super().clean()

    class Meta:
        model = InfantNvpDispensing
        fields = '__all__'
