from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantFuDxItemsForm, InfantFuDxForm
from ..models import InfantFuDx, InfantFuDxItems
from .modeladmin_mixins import CrfModelAdminMixin


class InfantFuDxItemsInline(TabularInlineMixin, admin.TabularInline):

    model = InfantFuDxItems
    form = InfantFuDxItemsForm
    extra = 0


@admin.register(InfantFuDxItems, site=td_infant_admin)
class InfantFuDxItemsAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuDxItemsForm

    fieldsets = (
        (None, {
            'fields': (
                'infant_fu_dx',
                'fu_dx',
                'fu_dx_specify',
                'health_facility',
                'was_hospitalized')
        }),
        audit_fieldset_tuple
    )

    radio_fields = {
        'health_facility': admin.VERTICAL,
        'was_hospitalized': admin.VERTICAL
    }

    search_fields = [
        'infant_fu_dx__infant_visit__appointment__registered_subject__subject_identifier',
        'infant_fu_dx__infant_visit__appointment__registered_subject__initials', ]


@admin.register(InfantFuDx, site=td_infant_admin)
class InfantFuDxAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuDxForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'infant_visit')
        }),
        audit_fieldset_tuple
    )

    inlines = [InfantFuDxItemsInline, ]
