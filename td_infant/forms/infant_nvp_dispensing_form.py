from td_infant_validators.form_validators import CrfOffStudyFormValidator
from td_infant_validators.form_validators import InfantNvpDispensingFormValidator

from ..models import InfantNvpDispensing
from .infant_form_mixin import InfantModelFormMixin


class InfantNvpDispensingForm(InfantModelFormMixin):

    form_validator_cls = InfantNvpDispensingFormValidator

    class Meta:
        model = InfantNvpDispensing
        fields = '__all__'
