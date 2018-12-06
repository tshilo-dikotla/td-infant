# from collections import OrderedDict

# from edc_export.actions import export_as_csv_action
# from edc_base.modeladmin_mixins import MembershipBaseModelAdmin
from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch

from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin, ModelAdminInstitutionMixin,
    audit_fieldset_tuple, ModelAdminNextUrlRedirectMixin,
    ModelAdminNextUrlRedirectError, ModelAdminReplaceLabelTextMixin)


# from ..models import InfantVisit


# from edc_export.actions import export_as_csv_action
class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin, ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            options.update(subject_identifier=obj.subject_identifier)
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


class BaseInfantScheduleModelAdmin(ModelAdminMixin, admin.ModelAdmin):

    search_fields = [
        'infant_visit__appointment__registered_subject__subject_identifier',
        'infant_visit__appointment__registered_subject__initials', ]


#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "infant_visit":
#             if request.GET.get('infant_visit'):
#                 kwargs["queryset"] = InfantVisit.objects.filter(
#                     id=request.GET.get('infant_visit'))
#         return super(BaseInfantScheduleModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
#
#     actions = [
#         export_as_csv_action(
#             description="Export CSV file",
#             fields=[],
#             delimiter=',',
#             exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created',
#                      'hostname_modified', 'infant_visit'],
#             extra_fields=OrderedDict(
#                 {'subject_identifier': 'infant_visit__appointment__registered_subject__subject_identifier',
#                  'gender': 'infant_visit__appointment__registered_subject__gender',
#                  'dob': 'infant_visit__appointment__registered_subject__dob',
#                  'registered': 'infant_visit__appointment__registered_subject__registration_datetime',
#                  'visit_code': 'infant_visit__appointment__visit_definition__code',
#                  'visit_reason': 'infant_visit__reason',
#                  'visit_study_status': 'infant_visit__study_status'
#                  }),
#         )]
