from .infant_form_mixin import InfantModelFormMixin
from ..models import SolidFoodAssessment


class SolidFoodAssessmentForm(InfantModelFormMixin):

    class Meta:
        model = SolidFoodAssessment
        fields = '__all__'
