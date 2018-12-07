from django import forms
from ..models import InfantFuPhysical


class InfantFuPhysicalForm(forms.ModelForm):

    class Meta:
        model = InfantFuPhysical
        fields = '__all__'
