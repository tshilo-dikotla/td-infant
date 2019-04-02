from django.test import TestCase
from edc_constants.constants import YES, NO

from ..models import KaraboSubjectScreening


class TestKaraboEligibility(TestCase):

    def setUp(self):
        self.options = {
            'infant_alive': YES,
            'infant_weight': YES,
            'major_anomalies': NO,
            'birth_complications': NO,
            'infant_documentation': YES,
            'infant_months': YES,
            'tb_treatment': NO,
            'incarcerated': YES,
            'willing_to_consent': YES
        }

    def test_infant_eligible(self):
        subject_screening = KaraboSubjectScreening(
            self.options)
        self.assertTrue(subject_screening.is_eligible)

    def test_infant_not_eligible(self):
        pass

