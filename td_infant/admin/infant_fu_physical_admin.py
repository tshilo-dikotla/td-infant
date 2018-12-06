from django.contrib import admin

from td_infant.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import td_infant_admin
from ..forms import InfantFuPhysicalForm
from ..models import InfantFuPhysical
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple


@admin.register(InfantFuPhysical, site=td_infant_admin)
class InfantFuPhysicalAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuPhysicalForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'height',
                'head_circumference',
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
                'neuro_exam_other'
            ]
        }

        ), audit_fieldset_tuple
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
