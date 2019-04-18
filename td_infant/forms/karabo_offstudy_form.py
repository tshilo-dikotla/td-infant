from django import forms
from ..models import KaraboOffstudy
from .form_mixins import SubjectModelFormMixin


class KaraboOffstudyForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = KaraboOffstudy
        fields = '__all__'
