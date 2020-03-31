from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_infant_admin
from ..forms import InfantFuDxItemsForm
from ..models import InfantFuDxItems
from .model_admin_mixins import ModelAdminMixin


@admin.register(InfantFuDxItems, site=td_infant_admin)
class InfantFuDxItemsAdmin(ModelAdminMixin, admin.ModelAdmin):
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
        audit_fieldset_tuple)

    radio_fields = {'health_facility': admin.VERTICAL,
                    'was_hospitalized': admin.VERTICAL}

    search_fields = ['infant_fu_dx__infant_visit__subject_identifier', ]
