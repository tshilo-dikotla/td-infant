from td_infant_validators.form_validators import InfantBirthDataFormValidator

from ..models import InfantBirthFeedingVaccine
from .infant_form_mixin import InfantModelFormMixin


class InfantBirthFeedinVaccineForm(InfantModelFormMixin):

    form_validator_cls = InfantBirthDataFormValidator

    class Meta:
        model = InfantBirthFeedingVaccine
        fields = '__all__'
