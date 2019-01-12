from .infant_form_mixin import InfantModelFormMixin
from ..models import SolidFoodAssessment

from td_infant_validators.form_validators import SolidFoodAssessementFormValidator


class SolidFoodAssessmentForm(InfantModelFormMixin):

    form_validator_cls = SolidFoodAssessementFormValidator

    class Meta:
        model = SolidFoodAssessment
        fields = '__all__'
