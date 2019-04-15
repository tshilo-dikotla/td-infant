from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import KaraboSubjectConsentForm
from ..models import KaraboSubjectConsent


@admin.register(KaraboSubjectConsent, site=td_infant_admin)
class KaraboSubjectConsentAdmin(admin.ModelAdmin):
    form = KaraboSubjectConsentForm

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'name',
                'surname',
                'initials',
                'consent_lang',
                'is_literate',
                'witness_name',
                'consent_datetime',
                'omang',
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'is_literate': admin.VERTICAL,
        'consent_reviewed': admin.VERTICAL,
        'study_questions': admin.VERTICAL,
        'assessment_score': admin.VERTICAL,
        'consent_signature': admin.VERTICAL,
        'consent_copy': admin.VERTICAL
    }
