from ..models import InfantArvProphMod
from .infant_form_mixin import InfantModelFormMixin


class InfantArvProphModForm(InfantModelFormMixin):
    
    pass

    class Meta:
        model = InfantArvProphMod
        fields = '__all__'
