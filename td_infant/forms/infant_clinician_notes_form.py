from django import forms

from ..models import InfantClinicianNotes, ClinicianNotesImage
from .form_mixins import InlineSubjectModelFormMixin
from .infant_form_mixin import InfantModelFormMixin


class InfantClinicianNotesForm(InfantModelFormMixin, forms.ModelForm):

    class Meta:
        model = InfantClinicianNotes
        fields = '__all__'


class ClinicianNotesImageForm(InlineSubjectModelFormMixin):

    class Meta:
        model = ClinicianNotesImage
        fields = '__all__'
