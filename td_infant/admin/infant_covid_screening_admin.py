from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantCovidScreeningForm
from ..models import InfantCovidScreening
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(InfantCovidScreening, site=td_infant_admin)
class InfantCovidScreeningAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
    form = InfantCovidScreeningForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'covid_tested',
                'covid_test_date',
                'is_test_date_estimated',
                'covid_results',
                'household_positive',
                'household_test_date',
                'is_household_test_estimated',
                'covid_contact',
                'covid_symptoms',
                'comments']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'covid_tested': admin.VERTICAL,
        'is_test_date_estimated': admin.VERTICAL,
        'covid_results': admin.VERTICAL,
        'household_positive': admin.VERTICAL,
        'is_household_test_estimated': admin.VERTICAL,
        'covid_contact': admin.VERTICAL}

    filter_horizontal = ('covid_symptoms',)
