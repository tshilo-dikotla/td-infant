from django.contrib import admin

from ..admin_site import td_infant_admin
from ..forms import InfantNvpAdjustmentForm
from ..models import InfantNvpAdjustment
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(InfantNvpAdjustment, site=td_infant_admin)
class InfantNvpAdjustmentAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = InfantNvpAdjustmentForm

    radio_fields = {
        'dose_adjustment': admin.VERTICAL,
        'dose_4_weeks': admin.VERTICAL}

    list_display = ('infant_visit', 'dose_adjustment', 'dose_4_weeks',)

    list_filter = ('dose_adjustment', 'dose_4_weeks',)
