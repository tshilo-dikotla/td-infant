from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantCrfModel


class InfantCrfModelForm(InfantModelFormMixin):

    class Meta:
        model = InfantCrfModel
        fields = '__all__'
