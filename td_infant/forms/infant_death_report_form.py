from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantDeathReport


class InfantDeathReportForm(InfantModelFormMixin):

    class Meta:
        model = InfantDeathReport
        fields = '__all__'
