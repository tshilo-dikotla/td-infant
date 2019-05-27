from td_infant_validators.form_validators import InfantFuDxFormValidator
from td_infant_validators.form_validators import InfantFuDxItemsFormValidator

from django.forms import ValidationError

from ..models import InfantFuDx, InfantFuDxItems
from .infant_form_mixin import InfantModelFormMixin


class InfantFuDxForm(InfantModelFormMixin):

    form_validator_cls = InfantFuDxFormValidator

    def clean(self):
        super().clean()
        infant_fu_dx = self.data.get('infantfudxitems_set-0-fu_dx')
        if not infant_fu_dx:
            raise ValidationError('Please fill the table below')

    class Meta:
        model = InfantFuDx
        fields = '__all__'


class InfantFuDxItemsForm(InfantModelFormMixin):

    form_validator_cls = InfantFuDxItemsFormValidator

    class Meta:
        model = InfantFuDxItems
        fields = '__all__'
