from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InfantVisit


class InfantVisitForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = InfantVisit
        fields = '__all__'
