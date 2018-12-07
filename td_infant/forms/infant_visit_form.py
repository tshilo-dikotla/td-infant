from django import forms
from ..models import InfantVisit


class InfantVisitForm(forms.ModelForm):

    class Meta:
        model = InfantVisit
        fields = '__all__'
