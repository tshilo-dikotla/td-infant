from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import td_infant_admin
from ..forms import KaraboTuberculosisHistoryForm
from ..models import KaraboTuberculosisHistory
from .karabo_modeladmin_mixins import KaraboCrfModelAdminMixin


@admin.register(KaraboTuberculosisHistory, site=td_infant_admin)
class KaraboTuberculosisHistoryAdmin(KaraboCrfModelAdminMixin, admin.ModelAdmin):
    form = KaraboTuberculosisHistoryForm

    fieldsets = (
        (None, {
            'fields': [
                'infant_visit',
                'report_datetime',
                'coughing',
                'coughing_rel',
                'other_coughing_rel',
                'fever',
                'fever_rel',
                'other_fever_rel',
                'weight_loss',
                'weight_loss_rel',
                'other_weight_loss',
                'night_sweats',
                'night_sweats_rel',
                'other_night_sweats',
                'diagnosis',
                'diagnosis_rel',
                'other_diagnosis_rel',
                'tb_exposure',
                'tb_exposure_det',
                'put_offstudy'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'coughing': admin.VERTICAL,
        'fever': admin.VERTICAL,
        'weight_loss': admin.VERTICAL,
        'diagnosis': admin.VERTICAL,
        'night_sweats': admin.VERTICAL,
        'diagnosis': admin.VERTICAL,
        'tb_exposure': admin.VERTICAL,
        'put_offstudy': admin.VERTICAL,
    }

    list_display = (
        'other_coughing_rel',
        'other_diagnosis_rel',
        'other_fever_rel',
        'other_weight_loss',
        'other_night_sweats',
        'other_diagnosis_rel',
        'tb_exposure_det')

    filter_horizontal = (
         'coughing_rel', 'fever_rel', 'weight_loss_rel',
         'night_sweats_rel', 'diagnosis_rel'
         )
