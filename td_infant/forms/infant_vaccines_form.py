from django import forms
from ..models import InfantVaccines


class InfantVaccinesForm(forms.ModelForm):

    class Meta:
        model = InfantVaccines
        fields = '__all__'
