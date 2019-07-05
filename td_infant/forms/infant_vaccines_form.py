from td_infant_validators.form_validators import CrfOffStudyFormValidator

from ..models import InfantVaccines
from .infant_form_mixin import InfantModelFormMixin


class InfantVaccinesForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantVaccines
        fields = '__all__'
