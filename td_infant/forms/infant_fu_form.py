from td_infant_validators.form_validators import CrfOffStudyFormValidator
from td_infant_validators.form_validators import InfantFuFormValidator

from ..models import InfantFu
from .infant_form_mixin import InfantModelFormMixin


class InfantFuForm(InfantModelFormMixin, CrfOffStudyFormValidator):

    form_validator_cls = InfantFuFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantFu
        fields = '__all__'
