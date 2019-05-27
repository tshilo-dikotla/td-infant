from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import td_infant_admin
from ..constants import INFANT
from ..forms import InfantVisitForm
from ..models import InfantVisit
from .model_admin_mixins import ModelAdminMixin


@admin.register(InfantVisit, site=td_infant_admin)
class InfantVisitAdmin(VisitModelAdminMixin,
                       ModelAdminMixin,
                       admin.ModelAdmin):

    form = InfantVisitForm
    dashboard_type = INFANT
    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'reason',
                'reason_missed',
                'study_status',
                'require_crfs',
                'info_source',
                'info_source_other',
                'information_provider',
                'information_provider_other',
                'is_present',
                'survival_status',
                'last_alive_date',
                'comments'
            ]}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple
    )

    radio_fields = {
        'reason': admin.VERTICAL,
        'study_status': admin.VERTICAL,
        'require_crfs': admin.VERTICAL,
        'info_source': admin.VERTICAL,
        'information_provider': admin.VERTICAL,
        'is_present': admin.VERTICAL,
        'survival_status': admin.VERTICAL
    }
