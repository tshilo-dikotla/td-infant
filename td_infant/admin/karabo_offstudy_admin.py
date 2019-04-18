from django.contrib import admin

from ..admin_site import td_infant_admin
from ..forms import KaraboOffstudyForm
from ..models import KaraboOffstudy
from .model_admin_mixins import InfantCrfModelAdminMixin


@admin.register(KaraboOffstudy, site=td_infant_admin)
class KaraboOffstudyAdmin(InfantCrfModelAdminMixin, admin.ModelAdmin):
    form = KaraboOffstudyForm
