from django.conf import settings
from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_fieldsets import FieldsetsModelAdminMixin
from edc_metadata import NextFormGetter
from import_export.admin import ImportExportActionModelAdmin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    FormAsJSONModelAdminMixin, ModelAdminRedirectOnDeleteMixin)

from edc_visit_tracking.modeladmin_mixins import (
    CrfModelAdminMixin as VisitTrackingCrfModelAdminMixin)


class KaraboModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                            ModelAdminFormInstructionsMixin,
                            ModelAdminFormAutoNumberMixin,
                            ModelAdminRevisionMixin,
                            ModelAdminAuditFieldsMixin,
                            ModelAdminReadOnlyMixin,
                            ModelAdminInstitutionMixin,
                            ModelAdminRedirectOnDeleteMixin,
                            ImportExportActionModelAdmin,
                            ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter


class KaraboCrfModelAdminMixin(VisitTrackingCrfModelAdminMixin,
                               KaraboModelAdminMixin,
                               FieldsetsModelAdminMixin,
                               FormAsJSONModelAdminMixin,
                               admin.ModelAdmin):

    show_save_next = True
    show_cancel = True

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'infant_subject_dashboard_url')

    def post_url_on_delete_kwargs(self, request, obj):
        return dict(
            subject_identifier=obj.infant_visit.subject_identifier,
            appointment=str(obj.infant_visit.appointment.id))

    def view_on_site(self, obj):
        dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
            'infant_subject_dashboard_url')
        try:
            url = reverse(
                dashboard_url_name, kwargs=dict(
                    subject_identifier=obj.infant_visit.subject_identifier,
                    appointment=str(obj.infant_visit.appointment.id)))
        except NoReverseMatch:
            url = super().view_on_site(obj)
        return url
