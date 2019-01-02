from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantBirthForm
from ..models import InfantBirth
from .model_admin_mixins import ModelAdminMixin


@admin.register(InfantBirth, site=td_infant_admin)
class InfantBirthAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = InfantBirthForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'first_name',
                'initials',
                'dob',
                'gender']}
         ), audit_fieldset_tuple)

    list_display = (
        'report_datetime',
        'first_name',
        'initials',
        'dob',
        'gender',
    )

    search_fields = ['infant_visit__subject_identifier', ]

    list_display = ('report_datetime', 'first_name')
    list_filter = ('gender',)
    radio_fields = {'gender': admin.VERTICAL}
