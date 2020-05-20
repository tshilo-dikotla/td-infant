from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fields

from ..admin_site import td_infant_admin
from ..forms import InfantClinicianNotesForm, ClinicianNotesImageForm
from ..models import InfantClinicianNotes, ClinicianNotesImage
from .model_admin_mixins import InfantCrfModelAdminMixin


class ClinicianNotesImageInline(TabularInlineMixin, admin.TabularInline):

    model = ClinicianNotesImage
    form = ClinicianNotesImageForm
    extra = 0

    fields = ('clinician_notes_image', audit_fields)

    readonly_fields = ('clinician_notes_image',)


@admin.register(InfantClinicianNotes, site=td_infant_admin)
class ClinicianNotesAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantClinicianNotesForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
            ]}
         ), )

    inlines = [ClinicianNotesImageInline]
