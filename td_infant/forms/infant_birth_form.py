from django import forms
from ..models import InfantBirth


class InfantBirthForm(forms.ModelForm):

    class Meta:
        model = InfantBirth
        fields = '__all__'
