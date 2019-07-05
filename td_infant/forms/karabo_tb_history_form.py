from td_infant_validators.form_validators import (
    KaraboTBHistoryFormValidator
)

from ..models import KaraboTuberculosisHistory
from .form_mixins import SubjectModelFormMixin


class KaraboTuberculosisHistoryForm(SubjectModelFormMixin):

    form_validator_cls = KaraboTBHistoryFormValidator

    class Meta:
        model = KaraboTuberculosisHistory
        fields = '__all__'
