from django import forms
from ..models import InfantBirthArv


class InfantBirthArvForm(forms.ModelForm):

    class Meta:
        model = InfantBirthArv
        fields = '__all__'
