from td_infant_validators.form_validators import CrfOffStudyFormValidator
from td_infant_validators.form_validators import InfantBirthArvFormValidator

from ..models import InfantBirthArv
from .infant_form_mixin import InfantModelFormMixin


class InfantBirthArvForm(InfantModelFormMixin):

    form_validator_cls = InfantBirthArvFormValidator

    class Meta:
        model = InfantBirthArv
        fields = '__all__'
