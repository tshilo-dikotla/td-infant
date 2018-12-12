from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fieldset_tuple
from ..admin_site import td_infant_admin
from ..forms import InfantFuImmunizationsForm, VaccinesReceivedForm, VaccinesMissedForm
from ..models import InfantFuImmunizations, VaccinesReceived, VaccinesMissed
from .model_admin_mixins import InfantCrfModelAdminMixin


class VaccinesReceivedInlineAdmin(TabularInlineMixin, admin.TabularInline):
    model = VaccinesReceived
    form = VaccinesReceivedForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'received_vaccine_name',
                'date_given',
                'infant_age')
        }),
    )


class VaccinesMissedInlineAdmin(TabularInlineMixin, admin.TabularInline):
    model = VaccinesMissed
    form = VaccinesMissedForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': (
                'missed_vaccine_name',
                'reason_missed',
                'reason_missed_other')
        }),
    )


@admin.register(InfantFuImmunizations, site=td_infant_admin)
class InfantFuImmunizationsAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuImmunizationsForm

    fieldsets = (
        (None, {
            'fields': (
                'infant_visit',
                'report_datetime',
                'vaccines_received',
                'vaccines_missed')
        }),
        audit_fieldset_tuple
    )

    inlines = [VaccinesReceivedInlineAdmin, VaccinesMissedInlineAdmin, ]
    radio_fields = {'vaccines_received': admin.VERTICAL,
                    'vaccines_missed': admin.VERTICAL}
