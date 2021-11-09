from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_odk.admin import StampImageActionMixin

from ..admin_site import td_infant_admin
from ..forms import InfantLabResultsFilesForm, LabResultsFileForm
from ..models import InfantLabResultsFiles, LabResultsFile
from .model_admin_mixins import InfantCrfModelAdminMixin


class LabResultsFileInline(TabularInlineMixin, admin.TabularInline):

    model = LabResultsFile
    form = LabResultsFileForm
    extra = 0

    fields = ('lab_results_preview', 'image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = (
            'lab_results_preview', 'datetime_captured', 'user_uploaded') + fields

        return fields


@admin.register(InfantLabResultsFiles, site=td_infant_admin)
class InfantLabResultsFilesAdmin(
        StampImageActionMixin, InfantCrfModelAdminMixin, admin.ModelAdmin):

    form = InfantLabResultsFilesForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
            ]}
         ), )

    inlines = [LabResultsFileInline]
