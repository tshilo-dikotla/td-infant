from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFeeding


class InfantFeedingForm(InfantModelFormMixin):

    class Meta:
        model = InfantFeeding
        fields = '__all__'
