from django import forms
from ..models import InfantNvpDispensing


class InfantNvpDispensingForm(forms.ModelForm):

    class Meta:
        model = InfantNvpDispensing
        fields = '__all__'
