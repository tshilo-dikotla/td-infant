from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantBirthFeedingVaccine


class InfantBirthFeedinVaccineForm(InfantModelFormMixin):

    class Meta:
        model = InfantBirthFeedingVaccine
        fields = '__all__'
