from ..models import InfantNvpDispensing
from .infant_form_mixin import InfantModelFormMixin


class InfantNvpDispensingForm(InfantModelFormMixin):

    class Meta:
        model = InfantNvpDispensing
        fields = '__all__'
