from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantArvProphForm, InfantArvProphModForm
from ..models import InfantArvProphMod, InfantArvProph
from .base_infant_scheduled_modeladmin import BaseInfantScheduleModelAdmin


class InfantArvProphModInline(TabularInlineMixin, admin.TabularInline):

    model = InfantArvProphMod
    form = InfantArvProphModForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'arv_code',
                'dose_status',
                'modification_date',
                'modification_code',
                'other_reason']}
         ),)


@admin.register(InfantArvProph, site=td_infant_admin)
class InfantArvProphAdmin(BaseInfantScheduleModelAdmin):

    form = InfantArvProphForm
    fieldsets = (
        (None, {
            'fields': [
                'prophylatic_nvp',
                'arv_status']}
         ), audit_fieldset_tuple)

    inlines = [InfantArvProphModInline, ]
    radio_fields = {
        'prophylatic_nvp': admin.VERTICAL,
        'arv_status': admin.VERTICAL,
    }


admin.site.register(InfantArvProph, InfantArvProphAdmin)


@admin.register(InfantArvProphAdmin, site=td_infant_admin)
class InfantArvProphModAdmin(BaseInfantScheduleModelAdmin):

    form = InfantArvProphModForm

    list_filter = ('infant_arv_proph',)

    fieldsets = (
        (None, {
            'fields': [
                'arv_code',
                'dose_status',
                'modification_date',
                'modification_code',
                'other_reason']}
         ), audit_fieldset_tuple)

    search_fields = [
        'infant_arv_proph__infant_visit__appointment__registered_subject__subject_identifier',
        'infant_arv_proph__infant_visit__appointment__registered_subject__initials', ]
