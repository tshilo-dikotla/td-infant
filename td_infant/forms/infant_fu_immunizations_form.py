from django.forms import forms
from .infant_form_mixin import InfantModelFormMixin
from edc_constants.constants import YES
from ..models import InfantFuImmunizations, VaccinesReceived, VaccinesMissed

from td_infant_validators.form_validators import (
    VaccinesMissedFormValidator, VaccinesReceivedFormValidator)


class InfantFuImmunizationsForm(InfantModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        vaccines_received = self.data.get(
            'vaccinesreceived_set-0-received_vaccine_name')
        if self.data.get('vaccines_received') == YES:
            if not vaccines_received:
                msg = {'vaccines_received':
                       'You mentioned that vaccines were received. Please '
                       'indicate which ones on the Received Vaccines table.'}
                raise forms.ValidationError(msg)
        else:
            if vaccines_received:
                raise forms.ValidationError('No vaccines received. Do not fill'
                                            ' Received Vaccines table')

        missed_vaccine_name = self.data.get(
            'vaccinesmissed_set-0-missed_vaccine_name')
        if self.data.get('vaccines_missed') == YES:
            if not missed_vaccine_name:
                msg = {'vaccines_missed':
                       'You mentioned that the child missed some '
                       'vaccines. Please indicate which ones in '
                       'the Missed Vaccines table.'}
                raise forms.ValidationError(msg)
        else:
            if missed_vaccine_name:
                raise forms.ValidationError(
                    'No vaccines missed. Do not fill Missed Vaccines table')
        return cleaned_data

    class Meta:
        model = InfantFuImmunizations
        fields = '__all__'


class VaccinesReceivedForm(InfantModelFormMixin):

    form_validator_cls = VaccinesReceivedFormValidator

    class Meta:
        model = VaccinesReceived
        fields = '__all__'


class VaccinesMissedForm(InfantModelFormMixin):

    form_validator_cls = VaccinesMissedFormValidator

    class Meta:
        model = VaccinesMissed
        fields = '__all__'
