from django import forms

from ..models import InfantLabResultsFiles, LabResultsFile
from .form_mixins import InlineSubjectModelFormMixin
from .infant_form_mixin import InfantModelFormMixin


class InfantLabResultsFilesForm(InfantModelFormMixin, forms.ModelForm):

    class Meta:
        model = InfantLabResultsFiles
        fields = '__all__'


class LabResultsFileForm(InlineSubjectModelFormMixin):

    class Meta:
        model = LabResultsFile
        fields = '__all__'
