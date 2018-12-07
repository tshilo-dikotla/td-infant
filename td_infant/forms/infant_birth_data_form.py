from ..models import InfantBirthData
from .infant_form_mixin import InfantModelFormMixin


class InfantBirthDataForm(InfantModelFormMixin):

    class Meta:
        model = InfantBirthData
        fields = '__all__'
