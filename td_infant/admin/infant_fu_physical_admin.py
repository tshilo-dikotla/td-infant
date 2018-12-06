from django.contrib import admin

from td_infant.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import td_infant_admin
from ..forms import InfantFuPhysicalForm
from ..models import InfantFuPhysical


@admin.register(InfantFuPhysical, site=td_infant_admin)
class InfantFuPhysicalAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = InfantFuPhysicalForm

    radio_fields = {
        'general_activity': admin.VERTICAL,
        'physical_exam_result': admin.VERTICAL,
        'heent_exam': admin.VERTICAL,
        'resp_exam': admin.VERTICAL,
        'cardiac_exam': admin.VERTICAL,
        'abdominal_exam': admin.VERTICAL,
        'skin_exam': admin.VERTICAL,
        'neurologic_exam': admin.VERTICAL
    }
