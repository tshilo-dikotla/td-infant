from django.contrib import admin
from edc_lab.admin import RequisitionAdminMixin
from edc_lab.admin import requisition_identifier_fields
from edc_lab.admin import requisition_identifier_fieldset, requisition_verify_fields
from edc_lab.admin import requisition_verify_fieldset
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantRequisitionForm
from ..models import InfantRequisition
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantRequisition, site=td_infant_admin)
class InfantRequisitionAdmin(
        InfantCrfModelAdminMixin, RequisitionAdminMixin,
        admin.ModelAdmin):

    form = InfantRequisitionForm

    ordering = ('requisition_identifier',)

    filter_horizontal = ('test_code',)

    fieldsets = (
        (None, {
            'fields': (
                'infant_visit',
                'requisition_datetime',
                'is_drawn',
                'reason_not_drawn',
                'reason_not_drawn_other',
                'drawn_datetime',
                'study_site',
                'panel',
                'test_code',
                'specimen_type',
                'item_type',
                'item_count',
                'estimated_volume',
                'priority',
                'comments',
            )}),
        requisition_identifier_fieldset,
        requisition_verify_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
        'priority': admin.VERTICAL,
        'study_site': admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj)
                + requisition_identifier_fields
                + requisition_verify_fields)