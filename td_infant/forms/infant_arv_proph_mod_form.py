from td_infant_validators.form_validators import CrfOffStudyFormValidator

from ..models import InfantArvProphMod
from .infant_form_mixin import InfantModelFormMixin


class InfantArvProphModForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantArvProphMod
        fields = '__all__'
