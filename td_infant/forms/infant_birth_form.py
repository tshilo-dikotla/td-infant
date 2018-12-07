from ..models import InfantBirth
from .infant_form_mixin import InfantModelFormMixin


class InfantBirthForm(InfantModelFormMixin):

    class Meta:
        model = InfantBirth
        fields = '__all__'
