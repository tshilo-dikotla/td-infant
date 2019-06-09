from td_infant_validators.form_validators import CrfOffStudyFormValidator

from ..models import InfantArvProphMod
from .infant_form_mixin import InfantModelFormMixin


class InfantArvProphModForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    def clean(self):
        super().clean()

    class Meta:
        model = InfantArvProphMod
        fields = '__all__'
