from django.contrib import admin

from td_infant.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import td_infant_admin
from ..constants import INFANT
from ..forms import InfantOffStudyForm
from ..models import InfantOffStudy


@admin.register(InfantOffStudy, site=td_infant_admin)
class InfantOffStudyAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = InfantOffStudyForm
    dashboard_type = INFANT
    visit_model_name = 'infantvisit'

    fields = (
        'infant_visit',
        'report_datetime',
        'offstudy_date',
        'reason',
        'reason_other',
        'comment',
    )

    list_display = (
        'infant_visit',
        'offstudy_date',
        'reason')
