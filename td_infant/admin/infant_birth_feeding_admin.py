from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantVaccinesForm, InfantBirthFeedinVaccineForm
from ..models import InfantBirthFeedingVaccine, InfantVaccines
from .model_admin_mixins import InfantCrfModelAdminMixin


class InfantVaccinesInline(TabularInlineMixin, admin.TabularInline):

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


@admin.register(InfantBirthFeedingVaccine, site=td_infant_admin)
class InfantBirthFeedingVaccineAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
    form = InfantBirthFeedinVaccineForm

    fieldsets = (
        (None, {
            'fields': [
                'report_datetime',
                'infant_visit',
                'feeding_after_delivery',
                'comments',
            ]
        }), audit_fieldset_tuple,
    )

    list_display = ('feeding_after_delivery',)

    list_filter = ('feeding_after_delivery',)

    inlines = [InfantVaccinesInline]

    radio_fields = {'feeding_after_delivery': admin.VERTICAL}


@admin.register(InfantVaccines, site=td_infant_admin)
class InfantVaccinesAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
    form = InfantVaccinesForm

    fieldsets = (
        (None, {
            'fields': (
                'infant_birth_feed_vaccine',
                'vaccination',
                'vaccine_date')
        }),
        audit_fieldset_tuple)

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
