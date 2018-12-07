from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFu


class InfantFuForm(InfantModelFormMixin):

    class Meta:
        model = InfantFu
        fields = '__all__'
