from collections import OrderedDict

from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from td_infant.admin.modeladmin_mixins import BaseInfantScheduleModelAdmin
from tshilo_dikotla.base_model_admin import BaseModelAdmin

from ..admin_site import td_infant_admin
from ..forms import InfantFuDxItemsForm
from ..models import InfantFuDx, InfantFuDxItems
from .modeladmin_mixins import CrfModelAdminMixin


class InfantFuDxItemsInline(TabularInlineMixin, admin.TabularInline):

    model = InfantFuDxItems
    form = InfantFuDxItemsForm
    extra = 0


@admin.register(InfantFuDxItems, site=td_infant_admin)
class InfantFuDxItemsAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuDxItemsForm

    search_fields = [
        'infant_fu_dx__infant_visit__appointment__registered_subject__subject_identifier',
        'infant_fu_dx__infant_visit__appointment__registered_subject__initials', ]


@admin.register(InfantFuDx, site=td_infant_admin)
class InfantFuDxAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    inlines = [InfantFuDxItemsInline, ]
