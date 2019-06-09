from td_infant_validators.form_validators import CrfOffStudyFormValidator
from td_infant_validators.form_validators import InfantNvpDispensingFormValidator

from ..models import InfantNvpDispensing
from .infant_form_mixin import InfantModelFormMixin


class InfantNvpDispensingForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    form_validator_cls = InfantNvpDispensingFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantNvpDispensing
        fields = '__all__'
