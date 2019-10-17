from django import forms

from ..models import InfantVaccines


class InfantVaccinesForm(forms.ModelForm):

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'infant_birth_feed_vaccine').infant_visit.appointment.subject_identifier
        super().clean()

    class Meta:
        model = InfantVaccines
        fields = '__all__'
