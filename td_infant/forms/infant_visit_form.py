from django import forms

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InfantVisit
from td_infant_validators.form_validators import InfantVisitFormValidator


class InfantVisitForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = InfantVisitFormValidator

    class Meta:
        model = InfantVisit
        fields = '__all__'
