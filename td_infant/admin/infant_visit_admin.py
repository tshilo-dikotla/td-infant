from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import td_infant_admin
from ..constants import INFANT
from ..forms import InfantVisitForm
from ..models import InfantVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(InfantVisit, site=td_infant_admin)
class InfantVisitAdmin(VisitModelAdminMixin,
                       ModelAdminMixin,
                       admin.ModelAdmin):

    form = InfantVisitForm
    dashboard_type = INFANT
#     requisition_model = InfantRequisition
    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'reason',
                'reason_unscheduled',
                'reason_unscheduled_other',
                'info_source',
                'info_source_other',
                'comments'
            ]}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple
    )

    radio_fields = {
        'reason': admin.VERTICAL,
        'reason_unscheduled': admin.VERTICAL,
        'info_source': admin.VERTICAL,
        'info_source': admin.VERTICAL}
