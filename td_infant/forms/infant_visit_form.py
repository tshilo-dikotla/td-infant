from .infant_form_mixin import InfantModelFormMixin
from ..models import InfantVisit


class InfantVisitForm(InfantModelFormMixin):

    class Meta:
        model = InfantVisit
        fields = '__all__'
