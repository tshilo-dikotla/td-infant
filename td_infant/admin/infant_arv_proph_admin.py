from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantArvProphForm, InfantArvProphModForm
from ..models import InfantArvProphMod, InfantArvProph
from .model_admin_mixins import InfantCrfModelAdminMixin, ModelAdminMixin


class InfantArvProphModInline(TabularInlineMixin, admin.TabularInline):

    model = InfantArvProphMod
    form = InfantArvProphModForm
    extra = 1

    fieldsets = (
        (None, {
            'fields': [
                'infant_arv_proph',
                'arv_code',
                'dose_status',
                'modification_date',
                'modification_code',
                'other_reason']}
         ),)


@admin.register(InfantArvProph, site=td_infant_admin)
class InfantArvProphAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantArvProphForm
    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'infant_visit',
                'prophylatic_nvp',
                'arv_status']}
         ), audit_fieldset_tuple)

    inlines = [InfantArvProphModInline, ]
    radio_fields = {
        'prophylatic_nvp': admin.VERTICAL,
        'arv_status': admin.VERTICAL,
    }


@admin.register(InfantArvProphMod, site=td_infant_admin)
class InfantArvProphModAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = InfantArvProphModForm

    list_filter = ('infant_arv_proph',)

    fieldsets = (
        (None, {
            'fields': [
                'infant_arv_proph',
                'arv_code',
                'dose_status',
                'modification_date',
                'modification_code',
                'other_reason']}
         ), audit_fieldset_tuple)

    search_fields = [
        'infant_arv_proph__infant_visit__subject_identifier',
        'infant_arv_proph__infant_visit__appointment__registered_subject__initials', ]
