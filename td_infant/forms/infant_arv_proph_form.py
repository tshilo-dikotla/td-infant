from django import forms
from ..models import InfantArvProph


class InfantArvProphForm(forms.ModelForm):

    class Meta:
        model = InfantArvProph
        fields = '__all__'
