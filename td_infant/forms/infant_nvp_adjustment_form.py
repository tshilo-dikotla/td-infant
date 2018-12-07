from django import forms

from ..models import InfantNvpAdjustment


class InfantNvpAdjustmentForm(forms.ModelForm):

    class Meta:
        model = InfantNvpAdjustment
        fields = '__all_'
