from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantFuDxItemsForm, InfantFuDxForm
from ..models import InfantFuDx, InfantFuDxItems
from .model_admin_mixins import InfantCrfModelAdminMixin


class InfantFuDxItemsInline(TabularInlineMixin, admin.TabularInline):

    model = InfantFuDxItems
    form = InfantFuDxItemsForm
    extra = 0


@admin.register(InfantFuDx, site=td_infant_admin)
class InfantFuDxAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
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
