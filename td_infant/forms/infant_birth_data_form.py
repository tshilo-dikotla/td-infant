from ..models import InfantBirthData
from .infant_form_mixin import InfantModelFormMixin

from td_infant_validators.form_validators import InfantBirthDataFormValidator


class InfantBirthDataForm(InfantModelFormMixin):

    orm_validator_cls = InfantBirthDataFormValidator

    class Meta:
        model = InfantBirthData
        fields = '__all__'
