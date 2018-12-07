from ..models import InfantFuPhysical
from .infant_form_mixin import InfantModelFormMixin


class InfantFuPhysicalForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuPhysical
        fields = '__all__'
