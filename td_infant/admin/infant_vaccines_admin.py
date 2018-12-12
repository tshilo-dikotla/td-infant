from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantVaccinesForm
from ..models import InfantVaccines
from .model_admin_mixins import ModelAdminMixin


@admin.register(InfantVaccines, site=td_infant_admin)
class InfantVaccinesAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = InfantVaccinesForm
    fieldsets = (
        (None, {
            'fields': [
                'infant_birth_feed_vaccine',
                'vaccination',
                'vaccine_date'
            ]
        }), audit_fieldset_tuple,
    )

    radio_fields = {'vaccination': admin.VERTICAL}
