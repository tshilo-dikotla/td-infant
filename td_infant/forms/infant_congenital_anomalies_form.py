from django import forms
from ..models import (InfantCongenitalAnomalies, InfantCardioDisorder,
                      InfantMusculoskeletal, InfantRenal, InfantFemaleGenital,
                      InfantCleftDisorder, InfantFacialDefect, InfantMouthUpGi,
                      InfantRespiratoryDefect, InfantLowerGi, InfantMaleGenital,
                      InfantSkin, InfantCns, InfantTrisomies)


class InfantCongenitalAnomaliesForm(forms.ModelForm):
    class Meta:
        model = InfantCongenitalAnomalies
        fields = '__all__'


class InfantFacialDefectForm(forms.ModelForm):
    class Meta:
        model = InfantFacialDefect
        fields = '__all__'


class InfantCleftDisorderForm(forms.ModelForm):
    class Meta:
        model = InfantCleftDisorder
        fields = '__all__'


class InfantMouthUpGiForm(forms.ModelForm):
    class Meta:
        model = InfantMouthUpGi
        fields = '__all__'


class InfantCardioDisorderForm(forms.ModelForm):
    class Meta:
        model = InfantCardioDisorder
        fields = '__all__'


class InfantRespiratoryDefectForm(forms.ModelForm):
    class Meta:
        model = InfantRespiratoryDefect
        fields = '__all__'


class InfantLowerGiForm(forms.ModelForm):
    class Meta:
        model = InfantLowerGi
        fields = '__all__'


class InfantFemaleGenitalForm(forms.ModelForm):
    class Meta:
        model = InfantFemaleGenital
        fields = '__all__'


class InfantMaleGenitalForm(forms.ModelForm):
    class Meta:
        model = InfantMaleGenital
        fields = '__all__'


class InfantRenalForm(forms.ModelForm):
    class Meta:
        model = InfantRenal
        fields = '__all__'


class InfantMusculoskeletalForm(forms.ModelForm):
    class Meta:
        model = InfantMusculoskeletal
        fields = '__all__'


class InfantSkinForm(forms.ModelForm):
    class Meta:
        model = InfantSkin
        fields = '__all__'


class InfantTrisomiesForm(forms.ModelForm):
    class Meta:
        model = InfantTrisomies
        fields = '__all__'


class InfantCnsForm(forms.ModelForm):
    class Meta:
        model = InfantCns
        fields = '__all__'
