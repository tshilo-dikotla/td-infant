from django.contrib import admin
from ..admin_site import td_infant_admin
from ..forms import InfantFuNewMedItemsForm
from ..models import InfantFuNewMedItems
from .model_admin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple


@admin.register(InfantFuNewMedItems, site=td_infant_admin)
class InfantFuNewMedItemsAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = InfantFuNewMedItemsForm

    fieldsets = (
        (None, {
            'fields': (
                'infant_fu_med',
                'medication',
                'other_medication',
                'date_first_medication',
                'stop_date',
                'drug_route',)
        }),
        audit_fieldset_tuple
    )
