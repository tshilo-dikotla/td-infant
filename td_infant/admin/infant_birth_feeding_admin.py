from collections import OrderedDict

from django.contrib import admin

from edc_base.modeladmin.admin import BaseTabularInline
from edc_export.actions import export_as_csv_action

from ..models import InfantBirthFeedingVaccine, InfantVaccines
from ..forms import InfantVaccinesForm, InfantBirthFeedinVaccineForm

from .base_infant_scheduled_modeladmin import BaseInfantScheduleModelAdmin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple


class InfantVaccinesInline(BaseTabularInline):

    model = InfantVaccines
    form = InfantVaccinesForm
    extra = 0

    fieldsets = (
        (None, {
            'fields': [
                'feeding_after_delivery',
                'comments'
            ]
        })
    )


class InfantBirthFeedingVaccineAdmin(BaseInfantScheduleModelAdmin):
    form = InfantBirthFeedinVaccineForm

    fieldsets = (
        (None, {
            'fields': [
                'vaccination',
                'vaccine_date'
            ]
        }), audit_fieldset_tuple,
    )

    list_display = ('feeding_after_delivery',)

    list_filter = ('feeding_after_delivery',)

    inlines = [InfantVaccinesInline]

    radio_fields = {'feeding_after_delivery': admin.VERTICAL}


admin.site.register(InfantBirthFeedingVaccine, InfantBirthFeedingVaccineAdmin)


class InfantVaccinesAdmin(admin.ModelAdmin):
    form = InfantVaccinesForm

    search_fields = [
        'infant_birth_feed_vaccine__infant_visit__appointment__registered_subject__subject_identifier',
        'infant_birth_feed_vaccine__infant_visit__appointment__registered_subject__initials']
#
#     actions = [
#         export_as_csv_action(
#             description="CSV Export of Infant Congenital Anomalies",
#             fields=[],
#             delimiter=',',
#             exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created',
#                      'hostname_modified'],
#             extra_fields=OrderedDict(
#                 {'subject_identifier':
#                  'infant_birth_feed_vaccine__infant_visit__appointment__registered_subject__subject_identifier',
#                  }),
#         )]
