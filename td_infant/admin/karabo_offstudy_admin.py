from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import KaraboOffstudyForm
from ..models import KaraboOffstudy
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(KaraboOffstudy, site=td_infant_admin)
class KaraboOffstudyAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = KaraboOffstudyForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'offstudy_date',
                'reason',
                'reason_other',
                'comment']}
         ), audit_fieldset_tuple)

    radio_fields = {'reason': admin.VERTICAL}
