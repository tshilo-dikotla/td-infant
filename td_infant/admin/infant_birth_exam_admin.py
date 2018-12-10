from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantBirthExamForm
from ..models import InfantBirthExam
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantBirthExam, site=td_infant_admin)
class InfantBirthExamAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
    form = InfantBirthExamForm

    fiedlsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'general_activity',
                'abnormal_activity',
                'physical_exam_result',
                'heent_exam',
                'heent_no_other',
                'resp_exam',
                'resp_exam_other',
                'cardiac_exam',
                'cardiac_exam_other',
                'abdominal_exam',
                'abdominal_exam_other',
                'skin_exam',
                'skin_exam_other',
                'neurologic_exam',
                'neuro_exam_other',
                'other_exam_info']}
         ), audit_fieldset_tuple)

    list_display = (
        'infant_visit',
        'general_activity',
        'physical_exam_result',
        'resp_exam',
    )

    list_filter = (
        'general_activity',
        'abnormal_activity',
        'physical_exam_result',
    )

    radio_fields = {
        'general_activity': admin.VERTICAL,
        'physical_exam_result': admin.VERTICAL,
        'heent_exam': admin.VERTICAL,
        'resp_exam': admin.VERTICAL,
        'cardiac_exam': admin.VERTICAL,
        'abdominal_exam': admin.VERTICAL,
        'skin_exam': admin.VERTICAL,
        'neurologic_exam': admin.VERTICAL
    }
