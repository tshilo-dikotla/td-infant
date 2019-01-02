from django import forms
from edc_lab.forms.modelform_mixins import RequisitionFormMixin

from ..models import InfantRequisition
from .infant_form_mixin import InfantModelFormMixin


class InfantRequisitionForm(InfantModelFormMixin, RequisitionFormMixin):

    requisition_identifier = forms.CharField(
        label='Requisition identifier'
    )

    class Meta:
        model = InfantRequisition
        fields = '__all__'
