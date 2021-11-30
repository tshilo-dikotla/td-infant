from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InfantLabResultsFiles, LabResultsFile


class InfantLabResultsFilesForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = InfantLabResultsFiles
        fields = '__all__'


class LabResultsFileForm(forms.ModelForm):

    class Meta:
        model = LabResultsFile
        fields = '__all__'
