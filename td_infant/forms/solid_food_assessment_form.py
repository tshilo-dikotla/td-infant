from django import forms
from ..models import SolidFoodAssessment


class SolidFoodAssessmentForm(forms.ModelForm):

    class Meta:
        model = SolidFoodAssessment
        fields = '__all__'
