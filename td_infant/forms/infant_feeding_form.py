from td_infant_validators.form_validators import InfantFeedingFormValidator

from ..models import InfantFeeding
from .infant_form_mixin import InfantModelFormMixin


class InfantFeedingForm(InfantModelFormMixin):

    form_validator_cls = InfantFeedingFormValidator

    class Meta:
        model = InfantFeeding
        fields = '__all__'
