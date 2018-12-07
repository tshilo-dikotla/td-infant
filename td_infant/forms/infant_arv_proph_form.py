from ..models import InfantArvProph
from .infant_form_mixin import InfantModelFormMixin


class InfantArvProphForm(InfantModelFormMixin):

    class Meta:
        model = InfantArvProph
        fields = '__all__'
