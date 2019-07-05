from td_infant_validators.form_validators import InfantBirthDataFormValidator

from ..models import InfantBirthData
from .infant_form_mixin import InfantModelFormMixin


class InfantBirthDataForm(InfantModelFormMixin):

    form_validator_cls = InfantBirthDataFormValidator

    class Meta:
        model = InfantBirthData
        fields = '__all__'
