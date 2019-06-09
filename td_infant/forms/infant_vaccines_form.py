from ..models import InfantVaccines
from .infant_form_mixin import InfantModelFormMixin


class InfantVaccinesForm(InfantModelFormMixin):

    def clean(self):
        super().clean()

    class Meta:
        model = InfantVaccines
        fields = '__all__'
