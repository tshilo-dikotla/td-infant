from td_infant_validators.form_validators import CrfOffStudyFormValidator

from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.modelform_mixins import VisitTrackingModelFormMixin

from ..models import InfantVisit


class InfantModelFormMixin(
        SiteModelFormMixin, VisitTrackingModelFormMixin,
        FormValidatorMixin, CrfOffStudyFormValidator , forms.ModelForm):

    visit_model = InfantVisit
