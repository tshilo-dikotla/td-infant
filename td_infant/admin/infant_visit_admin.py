from django.contrib import admin
# from edc_visit_tracking.admin import VisitAdminMixin

# from td_lab.models import InfantRequisition

from ..admin_site import td_infant_admin
from ..constants import INFANT
from ..forms import InfantVisitForm
from ..models import InfantVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(InfantVisit, site=td_infant_admin)
class InfantVisitAdmin(
        #         VisitAdminMixin,
        ModelAdminMixin):

    form = InfantVisitForm
    dashboard_type = INFANT
#     requisition_model = InfantRequisition
    visit_attr = 'infant_visit'
