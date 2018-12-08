from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantFuImmunizations, VaccinesReceived, VaccinesMissed


class InfantFuImmunizationsForm(InfantModelFormMixin):

    class Meta:
        model = InfantFuImmunizations
        fields = '__all__'


class VaccinesReceivedForm(InfantModelFormMixin):

    class Meta:
        model = VaccinesReceived
        fields = '__all__'


class VaccinesMissedForm(InfantModelFormMixin):

    class Meta:
        model = VaccinesMissed
        fields = '__all__'
