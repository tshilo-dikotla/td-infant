from td_infant_validators.form_validators import (
    VaccinesMissedFormValidator, VaccinesReceivedFormValidator)
from td_infant_validators.form_validators import CrfOffStudyFormValidator

from django.forms import forms
from edc_constants.constants import YES, OTHER

from ..models import InfantFuImmunizations, VaccinesReceived, VaccinesMissed
from .infant_form_mixin import InfantModelFormMixin


class InfantFuImmunizationsForm(InfantModelFormMixin,
                                CrfOffStudyFormValidator):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier

        super().clean()
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

        missed_vaccines = self.data.get('vaccinesmissed_set-TOTAL_FORMS')
        for i in range(int(missed_vaccines)):
            reason_missed = self.data.get(
                'vaccinesmissed_set-' + str(i) + '-reason_missed')
            other_reason = self.data.get(
                'vaccinesmissed_set-' + str(i) + '-reason_missed_other')

            if reason_missed == OTHER and not other_reason:
                message = {
                    'vaccines_missed': 'Please specify other reasons missed'
                    ' in the table below'
                }
                raise forms.ValidationError(message)

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
