from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from ..admin_site import td_infant_admin
from ..forms import InfantFuNewMedItemsForm, InfantFuNewMedForm
from ..models import InfantFuNewMed, InfantFuNewMedItems
from .modeladmin_mixins import CrfModelAdminMixin


class InfantFuNewMedItemsInline(TabularInlineMixin, admin.TabularInline):

    model = InfantFuNewMedItems
    form = InfantFuNewMedItemsForm
    extra = 0


@admin.register(InfantFuNewMedItems, site=td_infant_admin)
class InfantFuNewMedItemsAdmin(CrfModelAdminMixin):

    form = InfantFuNewMedItemsForm

    search_fields = [
        'infant_fu_med__infant_visit__appointment__registered_subject__subject_identifier',
        'infant_fu_med__infant_visit__appointment__registered_subject__initials', ]


@admin.register(InfantFuNewMed, site=td_infant_admin)
class InfantFuNewMedAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    radio_fields = {'new_medications': admin.VERTICAL, }
    inlines = [InfantFuNewMedItemsInline, ]
    form = InfantFuNewMedForm
