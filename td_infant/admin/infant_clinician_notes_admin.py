from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_odk.admin import StampImageActionMixin

from ..admin_site import td_infant_admin
from ..forms import InfantClinicianNotesForm, ClinicianNotesImageForm
from ..models import InfantClinicianNotes, ClinicianNotesImage
from .model_admin_mixins import InfantCrfModelAdminMixin


class ClinicianNotesImageInline(TabularInlineMixin, admin.TabularInline):

    model = ClinicianNotesImage
    form = ClinicianNotesImageForm
    extra = 0

    fields = ('clinician_notes_image', 'image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = (
            'clinician_notes_image', 'datetime_captured', 'user_uploaded') + fields

        return fields


@admin.register(InfantClinicianNotes, site=td_infant_admin)
class ClinicianNotesAdmin(
        StampImageActionMixin, InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantClinicianNotesForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
            ]}
         ), )

    inlines = [ClinicianNotesImageInline]

    search_fields = ('infant_visit__subject_identifier',)
