from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantOffScheduleForm
from ..models import InfantOffSchedule
from .model_admin_mixins import ModelAdminMixin


@admin.register(InfantOffSchedule, site=td_infant_admin)
class InfantOffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = InfantOffScheduleForm

    fieldsets = (
        (None, {
            'fields': [
                'schedule_name',
                'subject_identifier'
            ]}
         ), audit_fieldset_tuple)

    search_fields = ('subject_identifier',)

    list_filter = ('schedule_name', 'subject_identifier',)
