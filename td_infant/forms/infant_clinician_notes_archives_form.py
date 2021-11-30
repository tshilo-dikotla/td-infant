from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InfantClinicianNotesArchives, ClinicianNotesImageArchive


class InfantClinicianNotesArchivesForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = InfantClinicianNotesArchives
        fields = '__all__'


class ClinicianNotesImageArchiveForm(forms.ModelForm):

    class Meta:
        model = ClinicianNotesImageArchive
        fields = '__all__'
