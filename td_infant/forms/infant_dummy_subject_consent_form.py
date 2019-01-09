from django import forms
from django.conf import settings
from edc_base.sites import SiteModelFormMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..choices import STUDY_SITES
from ..models import InfantDummySubjectConsent


class InfantDummySubjectConsentForm(
        SiteModelFormMixin, FormValidatorMixin, ConsentModelFormMixin,
        forms.ModelForm):

    study_site = forms.ChoiceField(
        label='Study site',
        choices=STUDY_SITES,
        initial=settings.DEFAULT_STUDY_SITE,
        widget=forms.RadioSelect)

    class Meta:
        model = InfantDummySubjectConsent
        fields = '__all__'
