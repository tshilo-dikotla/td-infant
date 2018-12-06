from django.contrib import admin

from ..admin_site import td_infant_admin
from ..forms import InfantNvpDispensingForm
from ..models import InfantNvpDispensing
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(InfantNvpDispensing, site=td_infant_admin)
class InfantNvpDispensingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = InfantNvpDispensingForm

    radio_fields = {'nvp_prophylaxis': admin.VERTICAL,
                    'azt_prophylaxis': admin.VERTICAL,
                    'medication_instructions': admin.VERTICAL,
                    'correct_dose': admin.VERTICAL}

    list_display = ('infant_visit', 'nvp_prophylaxis',
                    'azt_prophylaxis', 'medication_instructions',)

    list_filter = ('nvp_prophylaxis', 'azt_prophylaxis', 'correct_dose',)
