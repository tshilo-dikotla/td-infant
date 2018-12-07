from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fieldset_tuple
from ..admin_site import td_infant_admin
from ..forms import InfantFuImmunizationsForm, VaccinesReceivedForm, VaccinesMissedForm
from ..models import InfantFuImmunizations, VaccinesReceived, VaccinesMissed
from td_infant.admin.model_admin_mixins import CrfModelAdminMixin


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
                'reason_missed')
        }),
    )


@admin.register(VaccinesReceived, site=td_infant_admin)
class VaccinesReceivedAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = VaccinesReceivedForm

    fieldsets = (
        (None, {
            'fields': (
                'received_vaccine_name',
                'date_given',
                'infant_age')
        }),
        audit_fieldset_tuple
    )

    search_fields = [
        'infant_fu_immunizations__infant_visit__appointment__registered_subject__subject_identifier',
        'infant_fu_immunizations__infant_visit__appointment__registered_subject__initials', ]


@admin.register(VaccinesMissed, site=td_infant_admin)
class VaccinesMissedAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = VaccinesMissedForm

    fieldsets = (
        (None, {
            'fields': (
                'missed_vaccine_name',
                'reason_missed')
        }),
        audit_fieldset_tuple
    )

    search_fields = [
        'infant_fu_immunizations__infant_visit__appointment__registered_subject__subject_identifier',
        'infant_fu_immunizations__infant_visit__appointment__registered_subject__initials', ]


@admin.register(InfantFuImmunizations, site=td_infant_admin)
class InfantFuImmunizationsAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuImmunizationsForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'infant_visit',
                'vaccines_received',
                'vaccines_missed')
        }),
        audit_fieldset_tuple
    )

    inlines = [VaccinesReceivedInlineAdmin, VaccinesMissedInlineAdmin, ]
    radio_fields = {'vaccines_received': admin.VERTICAL,
                    'vaccines_missed': admin.VERTICAL}
