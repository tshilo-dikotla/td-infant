from django.contrib import admin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import InfantBirthForm
from ..models import InfantBirth
from .modeladmin_mixins import ModelAdminMixin


@admin.register(InfantBirth, site=td_infant_admin)
class InfantBirthAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = InfantBirthForm

    fieldsets = (
        (None, {
            'fields': [
                'maternal_labour_del',
                'report_datetime',
                'first_name',
                'initials',
                'dob',
                'gender']}
         ), audit_fieldset_tuple)

    list_display = (
        'maternal_labour_del',
        'report_datetime',
        'first_name',
        'initials',
        'dob',
        'gender',
    )

    search_fields = ['infant_visit__subject_identifier', ]

    list_display = ('report_datetime', 'first_name', 'maternal_labour_del')
    list_filter = ('gender',)
    radio_fields = {'gender': admin.VERTICAL}

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "registered_subject":
#             if request.GET.get('registered_subject'):
#                 kwargs["queryset"] = RegisteredSubject.objects.filter(
#                     id__exact=request.GET.get('registered_subject', 0))
#         if db_field.name == "maternal_labour_del":
#             if request.GET.get('registered_subject'):
#                 maternal_subject_identifier = RegisteredSubject.objects.get(
#                     id=request.GET.get('registered_subject')).relative_identifier
#                 kwargs["queryset"] = MaternalLabourDel.objects.filter(
#                     registered_subject__subject_identifier=maternal_subject_identifier)
# return super(InfantBirthAdmin, self).formfield_for_foreignkey(db_field,
# request, **kwargs)
