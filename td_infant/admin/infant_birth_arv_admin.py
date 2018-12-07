from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..models import InfantBirthArv
from td_infant.admin.model_admin_mixins import CrfModelAdminMixin


@admin.register(InfantBirthArv, site=td_infant_admin)
class InfantBirthArvAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'azt_after_birth',
                'azt_dose_date',
                'azt_additional_dose',
                'sdnvp_after_birth',
                'nvp_dose_date',
                'azt_discharge_supply',
                'infant_arv_comments', ]}
         ), audit_fieldset_tuple)

    list_display = (
        'infant_visit', 'azt_after_birth',
        'azt_dose_date', 'azt_additional_dose',
        'sdnvp_after_birth',)

    list_filter = ('azt_after_birth', 'azt_dose_date',
                   'azt_additional_dose', 'sdnvp_after_birth',)

    radio_fields = {
        'azt_after_birth': admin.VERTICAL,
        'azt_additional_dose': admin.VERTICAL,
        'sdnvp_after_birth': admin.VERTICAL,
        'azt_discharge_supply': admin.VERTICAL,
    }
