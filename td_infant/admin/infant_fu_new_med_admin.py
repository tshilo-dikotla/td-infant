from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantFuNewMedItemsForm, InfantFuNewMedForm
from ..models import InfantFuNewMed, InfantFuNewMedItems
from .model_admin_mixins import InfantCrfModelAdminMixin


class InfantFuNewMedItemsInline(TabularInlineMixin, admin.TabularInline):

    model = InfantFuNewMedItems
    form = InfantFuNewMedItemsForm
    extra = 0

    fieldsets = (
        (None, {
            'fields': (
                'infant_fu_med',
                'medication',
                'other_medication',
                'date_first_medication',
                'stop_date',
                'drug_route')
        }), audit_fieldset_tuple
    )


@admin.register(InfantFuNewMed, site=td_infant_admin)
class InfantFuNewMedAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantFuNewMedForm

    fieldsets = (
        (None, {
            'fields': (
                'infant_visit',
                'report_datetime',
                'new_medications')
        }),
    )

    radio_fields = {'new_medications': admin.VERTICAL, }
    inlines = [InfantFuNewMedItemsInline, ]
