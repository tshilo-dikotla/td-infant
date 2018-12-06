from django.contrib import admin

from ..admin_site import td_infant_admin
from ..forms import InfantFuForm
from ..models import InfantFu
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(InfantFu, site=td_infant_admin)
class InfantFuAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuForm

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
