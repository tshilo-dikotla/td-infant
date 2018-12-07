from .infant_form_mixin import InfantModelFormMixin
from ..models import (InfantCongenitalAnomalies, InfantCardioDisorder,
                      InfantMusculoskeletal, InfantRenal, InfantFemaleGenital,
                      InfantCleftDisorder, InfantFacialDefect, InfantMouthUpGi,
                      InfantRespiratoryDefect, InfantLowerGi, InfantMaleGenital,
                      InfantSkin, InfantCns, InfantTrisomies)


class InfantCongenitalAnomaliesForm(InfantModelFormMixin):
    class Meta:
        model = InfantCongenitalAnomalies
        fields = '__all__'


class InfantFacialDefectForm(InfantModelFormMixin):
    class Meta:
        model = InfantFacialDefect
        fields = '__all__'


class InfantCleftDisorderForm(InfantModelFormMixin):
    class Meta:
        model = InfantCleftDisorder
        fields = '__all__'


class InfantMouthUpGiForm(InfantModelFormMixin):
    class Meta:
        model = InfantMouthUpGi
        fields = '__all__'


class InfantCardioDisorderForm(InfantModelFormMixin):
    class Meta:
        model = InfantCardioDisorder
        fields = '__all__'


class InfantRespiratoryDefectForm(InfantModelFormMixin):
    class Meta:
        model = InfantRespiratoryDefect
        fields = '__all__'


class InfantLowerGiForm(InfantModelFormMixin):
    class Meta:
        model = InfantLowerGi
        fields = '__all__'


class InfantFemaleGenitalForm(InfantModelFormMixin):
    class Meta:
        model = InfantFemaleGenital
        fields = '__all__'


class InfantMaleGenitalForm(InfantModelFormMixin):
    class Meta:
        model = InfantMaleGenital
        fields = '__all__'


class InfantRenalForm(InfantModelFormMixin):
    class Meta:
        model = InfantRenal
        fields = '__all__'


class InfantMusculoskeletalForm(InfantModelFormMixin):
    class Meta:
        model = InfantMusculoskeletal
        fields = '__all__'


class InfantSkinForm(InfantModelFormMixin):
    class Meta:
        model = InfantSkin
        fields = '__all__'


class InfantTrisomiesForm(InfantModelFormMixin):
    class Meta:
        model = InfantTrisomies
        fields = '__all__'


class InfantCnsForm(InfantModelFormMixin):
    class Meta:
        model = InfantCns
        fields = '__all__'
