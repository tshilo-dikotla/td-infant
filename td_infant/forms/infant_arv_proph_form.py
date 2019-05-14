from django.core.exceptions import ValidationError
from edc_constants.constants import YES, OTHER
from ..models import InfantArvProph
from .infant_form_mixin import InfantModelFormMixin
from ..constants import START, MODIFIED, NEVER_STARTED
from td_infant_validators.form_validators import InfantArvProphFormValidator


class InfantArvProphForm(InfantModelFormMixin):

    form_validator_cls = InfantArvProphFormValidator

    def clean(self):
        cleaned_data = super().clean()
        arv_proph_mod = self.data.get(
            'infantarvprophmod_set-0-arv_code')
        if cleaned_data.get('prophylatic_nvp') == YES:
            if cleaned_data.get('arv_status') in [START, MODIFIED] and not arv_proph_mod:
                message = {
                    'arv_status': 'Please complete the infant arv proph mods table.'
                }
                raise ValidationError(message)
            if cleaned_data.get('arv_status') == NEVER_STARTED and arv_proph_mod:
                message = {
                    'arv_status': 'Infant never started prophlaxis, '
                    'do not complete the infant arv proph mods table.'}
                raise ValidationError(message)

            total_prophmod = self.data.get('infantarvprophmod_set-TOTAL_FORMS')
            for i in range(int(total_prophmod)):
                modification_code = self.data.get(
                    'infantarvprophmod_set-' + str(i) + '-modification_code')
                other_reason = self.data.get(
                    'infantarvprophmod_set-' + str(i) + '-other_reason')
                if modification_code == OTHER and not other_reason:
                    message = {
                        'arv_status': 'Please specify other reasons'
                        ' in the table below'
                    }
                    raise ValidationError(message)

    class Meta:
        model = InfantArvProph
        fields = '__all__'
