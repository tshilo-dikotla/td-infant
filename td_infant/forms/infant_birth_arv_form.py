from ..models import InfantBirthArv
from .infant_form_mixin import InfantModelFormMixin


class InfantBirthArvForm(InfantModelFormMixin):

    class Meta:
        model = InfantBirthArv
        fields = '__all__'
