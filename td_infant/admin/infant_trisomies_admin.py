from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantTrisomiesForm
from ..models import InfantTrisomies
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantTrisomies, site=td_infant_admin)
class InfantTrisomiesAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantTrisomiesForm

    fieldsets = (
        (None, {
            'fields': [
                'congenital_anomalies',
                'trisomies',
                'abnormality_status',
                'trisomies_other',
            ]
        }

        ), audit_fieldset_tuple,
    )

    radio_fields = {
        'trisomies': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }
