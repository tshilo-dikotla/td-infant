from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_infant_admin
from ..forms import InfantNvpAdjustmentForm
from ..models import InfantNvpAdjustment
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantNvpAdjustment, site=td_infant_admin)
class InfantNvpAdjustmentAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantNvpAdjustmentForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'dose_adjustment',
                'adjusted_dose',
                'dose_4_weeks',
                'incomplete_dose']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'dose_adjustment': admin.VERTICAL,
        'dose_4_weeks': admin.VERTICAL}

    list_display = ('infant_visit', 'dose_adjustment', 'dose_4_weeks',)

    list_filter = ('dose_adjustment', 'dose_4_weeks',)
