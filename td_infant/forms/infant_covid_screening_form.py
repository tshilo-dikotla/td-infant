from td_infant_validators.form_validators import InfantCovidScreeningFormValidator

from ..models import InfantCovidScreening
from .infant_form_mixin import InfantModelFormMixin


class InfantCovidScreeningForm(InfantModelFormMixin):

    form_validator_cls = InfantCovidScreeningFormValidator

    class Meta:
        model = InfantCovidScreening
        fields = '__all__'
