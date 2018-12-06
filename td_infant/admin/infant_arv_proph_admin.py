from collections import OrderedDict

from django.contrib import admin

from edc_base.modeladmin.admin import BaseTabularInline
from edc_export.actions import export_as_csv_action

from ..models import InfantArvProphMod, InfantArvProph
from ..forms import InfantArvProphForm, InfantArvProphModForm

from .base_infant_scheduled_modeladmin import BaseInfantScheduleModelAdmin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple


class InfantArvProphModInline(BaseTabularInline):

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

    actions = [
        export_as_csv_action(
            description="CSV Export of Infant NVP or AZT Proph",
            fields=[],
            delimiter=',',
            exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created',
                     'hostname_modified'],
            extra_fields=OrderedDict(
                {'subject_identifier': 'infant_arv_proph__infant_visit__appointment__registered_subject__subject_identifier',
                 'gender': 'infant_arv_proph__infant_visit__appointment__registered_subject__gender',
                 'dob': 'infant_arv_proph__infant_visit__appointment__registered_subject__dob',
                 }),
        )]


admin.site.register(InfantArvProphMod, InfantArvProphModAdmin)
