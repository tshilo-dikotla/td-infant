from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantVaccinesForm, InfantBirthFeedinVaccineForm
from ..models import InfantBirthFeedingVaccine, InfantVaccines
from .model_admin_mixins import InfantCrfModelAdminMixin


class InfantVaccinesInline(TabularInlineMixin, admin.TabularInline):

    model = InfantVaccines
    form = InfantVaccinesForm
    extra = 0

    fieldsets = (
        ['Infant Vaccines', {
            'fields': (
                'infant_birth_feed_vaccine',
                'vaccination',
                'vaccine_date')},
         ], audit_fieldset_tuple)


@admin.register(InfantBirthFeedingVaccine, site=td_infant_admin)
class InfantBirthFeedingVaccineAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantBirthFeedinVaccineForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'feeding_after_delivery',
                'comments',
            ]
        }),
    )

    list_display = ('feeding_after_delivery',)

    list_filter = ('feeding_after_delivery',)

    inlines = [InfantVaccinesInline]

    radio_fields = {'feeding_after_delivery': admin.VERTICAL}
