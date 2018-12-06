# from django.contrib import admin
# from edc_model_admin import TabularInlineMixin
#
# from ..admin_site import td_infant_admin
# from ..forms import InfantFuImmunizationsForm, VaccinesReceivedForm, VaccinesMissedForm
# from ..models import InfantFuImmunizations, VaccinesReceived, VaccinesMissed
# from .modeladmin_mixins import CrfModelAdminMixin
#
#
# class VaccinesReceivedInlineAdmin(TabularInlineMixin, admin.TabularInline):
#     model = VaccinesReceived
#     form = VaccinesReceivedForm
#     extra = 1
#
#
# class VaccinesMissedInlineAdmin(TabularInlineMixin, admin.TabularInline):
#     model = VaccinesMissed
#     form = VaccinesMissedForm
#     extra = 1
#
#
# @admin.register(VaccinesReceived, site=td_infant_admin)
# class VaccinesReceivedAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#     form = VaccinesReceivedForm
#
#     search_fields = [
#         'infant_fu_immunizations__infant_visit__appointment__registered_subject__subject_identifier',
#         'infant_fu_immunizations__infant_visit__appointment__registered_subject__initials', ]
#
#
# @admin.register(VaccinesMissed, site=td_infant_admin)
# class VaccinesMissedAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#     form = VaccinesMissedForm
#
#     search_fields = [
#         'infant_fu_immunizations__infant_visit__appointment__registered_subject__subject_identifier',
#         'infant_fu_immunizations__infant_visit__appointment__registered_subject__initials', ]
#
#
# @admin.register(InfantFuImmunizations, site=td_infant_admin)
# class InfantFuImmunizationsAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#     form = InfantFuImmunizationsForm
#     inlines = [VaccinesReceivedInlineAdmin, VaccinesMissedInlineAdmin, ]
#     radio_fields = {'vaccines_received': admin.VERTICAL,
#                     'vaccines_missed': admin.VERTICAL}
