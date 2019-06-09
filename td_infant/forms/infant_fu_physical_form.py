from td_infant_validators.form_validators import InfantFuPhysicalFormValidator

from ..models import InfantFuPhysical
from .infant_form_mixin import InfantModelFormMixin


class InfantFuPhysicalForm(InfantModelFormMixin):

    form_validator_cls = InfantFuPhysicalFormValidator

    def clean(self):
        super().clean()

    class Meta:
        model = InfantFuPhysical
        fields = '__all__'
