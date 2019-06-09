from td_infant_validators.form_validators import CrfOffStudyFormValidator
from td_infant_validators.form_validators import InfantFuPhysicalFormValidator

from ..models import InfantFuPhysical
from .infant_form_mixin import InfantModelFormMixin


class InfantFuPhysicalForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    form_validator_cls = InfantFuPhysicalFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantFuPhysical
        fields = '__all__'
