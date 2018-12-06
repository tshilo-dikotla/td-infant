from django.contrib import admin

from ..admin_site import td_infant_admin
from ..forms import InfantBirthDataForm
from ..models import InfantBirthData
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(InfantBirthData, site=td_infant_admin)
class InfantBirthDataAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = InfantBirthDataForm

    fields = (
        "infant_visit",
        "weight_kg",
        "infant_length",
        "head_circumference",
        "apgar_score",
        "apgar_score_min_1",
        "apgar_score_min_5",
        "apgar_score_min_10",
        "congenital_anomalities",
        "other_birth_info")

    radio_fields = {
        "apgar_score": admin.VERTICAL,
        "congenital_anomalities": admin.VERTICAL}
