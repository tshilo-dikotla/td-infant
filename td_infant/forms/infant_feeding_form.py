from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFeeding

from td_infant_validators.form_validators import InfantFeedingFormValidator


class InfantFeedingForm(InfantModelFormMixin):

    form_validator_cls = InfantFeedingFormValidator

    class Meta:
        model = InfantFeeding
        fields = '__all__'
