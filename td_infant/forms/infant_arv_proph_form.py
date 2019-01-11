from django.core.exceptions import ValidationError
from edc_constants.constants import YES
from ..models import InfantArvProph
from .infant_form_mixin import InfantModelFormMixin
from ..constants import START, MODIFIED, NEVER_STARTED


class InfantArvProphForm(InfantModelFormMixin):

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

    class Meta:
        model = InfantArvProph
        fields = '__all__'
