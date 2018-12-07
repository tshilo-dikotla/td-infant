from ..models import InfantNvpAdjustment
from .infant_form_mixin import InfantModelFormMixin


class InfantNvpAdjustmentForm(InfantModelFormMixin):

    class Meta:
        model = InfantNvpAdjustment
        fields = '__all__'
