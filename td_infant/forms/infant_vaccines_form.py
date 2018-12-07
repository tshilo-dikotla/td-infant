from ..models import InfantVaccines
from .infant_form_mixin import InfantModelFormMixin


class InfantVaccinesForm(InfantModelFormMixin):

    class Meta:
        model = InfantVaccines
        fields = '__all__'
