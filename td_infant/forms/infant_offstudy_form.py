from ..models import InfantOffStudy
from .infant_form_mixin import InfantModelFormMixin


class InfantOffStudyForm(InfantModelFormMixin):

    class Meta:
        model = InfantOffStudy
        fields = '__all__'
