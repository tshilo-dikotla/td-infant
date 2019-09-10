from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import InfantOffSchedule


class InfantOffScheduleForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = InfantOffSchedule
        fields = '__all__'
