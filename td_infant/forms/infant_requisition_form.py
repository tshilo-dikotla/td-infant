from django import forms
from edc_lab.forms.modelform_mixins import RequisitionFormMixin

from td_infant_validators.form_validators import InfantFormValidatorMixin
from ..models import InfantRequisition
from .infant_form_mixin import InfantModelFormMixin


class InfantRequisitionForm(InfantFormValidatorMixin,
                            InfantModelFormMixin, RequisitionFormMixin):

    requisition_identifier = forms.CharField(
        label='Requisition identifier'
    )

    def clean(self):
        super().clean()
        self.validate_against_visit_datetime(
            self.cleaned_data.get('requisition_datetime'))

    class Meta:
        model = InfantRequisition
        fields = '__all__'
