from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantArvProphMod


class InfantArvProphModForm(InfantModelFormMixin):

    class Meta:
        model = InfantArvProphMod
        fields = '__all__'
