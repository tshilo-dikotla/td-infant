from django.contrib import admin

from ..admin_site import td_infant_admin
from ..models import InfantOffSchedule
from .model_admin_mixins import ModelAdminMixin


@admin.register(InfantOffSchedule, site=td_infant_admin)
class InfantOffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):

    pass
