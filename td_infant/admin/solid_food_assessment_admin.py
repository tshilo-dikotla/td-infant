from django.contrib import admin
from ..admin_site import td_infant_admin
from ..forms import SolidFoodAssessmentForm
from ..models import SolidFoodAssessment
from .modeladmin_mixins import CrfModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple


@admin.register(SolidFoodAssessment, site=td_infant_admin)
class SolidFoodAssessmentAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = SolidFoodAssessmentForm

    fieldsets = (
        (None, {
            'fields': [
                ''
                'age_solid_food',
                'solid_foods',
                'solid_foods_other',
                'porridge',
                'porridge_freq',
                'tsabana',
                'tsabana_week',
                'mother_tsabana',
                'meat',
                'meat_freq',
                'potatoes',
                'potatoes_freq',
                'carrot_swt_potato',
                'carrot_swt_potato_freq',
                'green_veg',
                'green_veg_freq',
                'fresh_fruits',
                'fresh_fruits_freq',
                'fullcream_milk',
                'fullcream_milk_freq',
                'skim_milk',
                'skim_milk_freq',
                'raw_milk',
                'raw_milk_freq',
                'juice',
                'juice_freq',
                'eggs',
                'eggs_freq',
                'yogurt',
                'yogurt_freq',
                'cheese',
                'cheese_freq',
                'rations',
                'rations_receviced'
            ]
        }), audit_fieldset_tuple
    )

    radio_fields = {'porridge': admin.VERTICAL,
                    'tsabana': admin.VERTICAL,
                    'mother_tsabana': admin.VERTICAL,
                    'meat': admin.VERTICAL,
                    'potatoes': admin.VERTICAL,
                    'carrot_swt_potato': admin.VERTICAL,
                    'green_veg': admin.VERTICAL,
                    'fresh_fruits': admin.VERTICAL,
                    'fullcream_milk': admin.VERTICAL,
                    'skim_milk': admin.VERTICAL,
                    'raw_milk': admin.VERTICAL,
                    'juice': admin.VERTICAL,
                    'eggs': admin.VERTICAL,
                    'yogurt': admin.VERTICAL,
                    'cheese': admin.VERTICAL,
                    'rations': admin.VERTICAL,
                    }
    filter_horizontal = ('solid_foods', 'rations_receviced')
