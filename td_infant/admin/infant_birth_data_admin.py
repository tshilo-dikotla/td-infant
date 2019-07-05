from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_infant_admin
from ..forms import InfantBirthDataForm
from ..models import InfantBirthData
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantBirthData, site=td_infant_admin)
class InfantBirthDataAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantBirthDataForm

    fieldsets = (
        (None, {
            'fields': (
                'infant_visit',
                'report_datetime',
                'weight_kg',
                'infant_length',
                'head_circumference',
                'apgar_score',
                'apgar_score_min_1',
                'apgar_score_min_5',
                'apgar_score_min_10',
                'congenital_anomalities',
                'other_birth_info')}
         ), audit_fieldset_tuple)

    radio_fields = {
        'apgar_score': admin.VERTICAL,
        'congenital_anomalities': admin.VERTICAL}
