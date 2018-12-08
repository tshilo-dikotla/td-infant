from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantBirthExam


class InfantBirthExamForm(InfantModelFormMixin):

    class Meta:
        model = InfantBirthExam
        fields = '__all__'
