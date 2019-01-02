from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InfantVisit


class InfantModelFormMixin(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    visit_model = InfantVisit
