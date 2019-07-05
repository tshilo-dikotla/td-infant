from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_infant_admin
from ..forms import InfantNvpDispensingForm
from ..models import InfantNvpDispensing
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantNvpDispensing, site=td_infant_admin)
class InfantNvpDispensingAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantNvpDispensingForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'nvp_prophylaxis',
                'reason_not_given',
                'azt_prophylaxis',
                'azt_dose_given',
                'nvp_admin_date',
                'medication_instructions',
                'dose_admin_infant',
                'correct_dose',
                'corrected_dose']}
         ), audit_fieldset_tuple)

    radio_fields = {'nvp_prophylaxis': admin.VERTICAL,
                    'azt_prophylaxis': admin.VERTICAL,
                    'medication_instructions': admin.VERTICAL,
                    'correct_dose': admin.VERTICAL}

    list_display = ('infant_visit', 'nvp_prophylaxis',
                    'azt_prophylaxis', 'medication_instructions',)

    list_filter = ('nvp_prophylaxis', 'azt_prophylaxis', 'correct_dose',)
