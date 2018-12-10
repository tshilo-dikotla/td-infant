from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_infant_admin
from ..forms import InfantFuForm
from ..models import InfantFu
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantFu, site=td_infant_admin)
class InfantFuAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'infant_visit',
                'physical_assessment',
                'diarrhea_illness',
                'has_dx',
                'was_hospitalized',
                'days_hospitalized')
        }),
        audit_fieldset_tuple)

    list_display = (
        'physical_assessment',
        'diarrhea_illness',
        'has_dx',
        'was_hospitalized',
        'days_hospitalized',
    )

    radio_fields = {
        'physical_assessment': admin.VERTICAL,
        'diarrhea_illness': admin.VERTICAL,
        'has_dx': admin.VERTICAL,
        'was_hospitalized': admin.VERTICAL,
    }
