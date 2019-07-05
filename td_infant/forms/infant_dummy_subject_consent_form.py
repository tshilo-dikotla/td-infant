from django import forms
from django.conf import settings
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from edc_consent.modelform_mixins import ConsentModelFormMixin
from td_infant_validators.form_validators import CrfOffStudyFormValidator

from ..choices import STUDY_SITES
from ..models import InfantDummySubjectConsent


class InfantDummySubjectConsentForm(
        SiteModelFormMixin, FormValidatorMixin, CrfOffStudyFormValidator,
        ConsentModelFormMixin, forms.ModelForm):

    study_site = forms.ChoiceField(
        label='Study site',
        choices=STUDY_SITES,
        initial=settings.DEFAULT_STUDY_SITE,
        widget=forms.RadioSelect)

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_visit').appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantDummySubjectConsent
        fields = '__all__'
