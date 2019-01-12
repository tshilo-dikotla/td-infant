from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantBirthExam

from td_infant_validators.form_validators import InfantBirthExamFormValidator


class InfantBirthExamForm(InfantModelFormMixin):

    form_validator_cls = InfantBirthExamFormValidator

    class Meta:
        model = InfantBirthExam
        fields = '__all__'
