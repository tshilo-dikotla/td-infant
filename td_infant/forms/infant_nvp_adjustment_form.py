from td_infant_validators.form_validators import (
    InfantNvpAdjustmentFormValidator)
from td_infant_validators.form_validators import CrfOffStudyFormValidator

from ..models import InfantNvpAdjustment
from .infant_form_mixin import InfantModelFormMixin


class InfantNvpAdjustmentForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    form_validator_cls = InfantNvpAdjustmentFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantNvpAdjustment
        fields = '__all__'
