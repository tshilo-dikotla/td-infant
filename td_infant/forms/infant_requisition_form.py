from arrow.arrow import Arrow
from django import forms
from django.conf import settings
from django.utils import timezone
from edc_base.utils import convert_php_dateformat
from edc_form_validators import FormValidatorMixin

from edc_lab.forms.modelform_mixins import RequisitionFormMixin
from td_infant_validators.form_validators import InfantRequisitionFormValidator

from ..models import InfantRequisition
from .infant_form_mixin import InfantModelFormMixin


class InfantRequisitionForm(InfantModelFormMixin, RequisitionFormMixin,
                            FormValidatorMixin):

    form_validator_cls = InfantRequisitionFormValidator

    requisition_identifier = forms.CharField(
        label='Requisition identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        self.validate_requisition_datetime()
        super().clean()

    def validate_requisition_datetime(self):
        requisition_datetime = self.cleaned_data.get('requisition_datetime')
        maternal_visit = self.cleaned_data.get('infant_visit')
        if requisition_datetime:
            requisition_datetime = Arrow.fromdatetime(
                requisition_datetime, requisition_datetime.tzinfo).to('utc').datetime
            if requisition_datetime < maternal_visit.report_datetime:
                formatted = timezone.localtime(maternal_visit.report_datetime).strftime(
                    convert_php_dateformat(settings.SHORT_DATETIME_FORMAT))
                raise forms.ValidationError({
                    'requisition_datetime':
                    f'Invalid. Cannot be before date of visit {formatted}.'})

    def validate_other_specify_field(self, form_validator=None):
        form_validator.validate_other_specify(
            field='reason_not_drawn', other_stored_value='other')

    class Meta:
        model = InfantRequisition
        fields = '__all__'
