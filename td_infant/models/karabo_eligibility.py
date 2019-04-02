from django.apps import apps as django_apps
from edc_constants.constants import YES, NO


class KaraboEligibility:

    infant_bith_data = 'td_infant.infantbirthdata'

    def __init__(self, infant_alive=None, infant_weight=None,
                 major_anomalies=None, birth_complications=None,
                 infant_documentation=None, infant_months=None,
                 tb_treatment=None, incarcerated=None,
                 willing_to_consent=None, subject_identifier=None):

        self.eligible = True
        self.reasons_ineligible = []
        self.subject_identifier = subject_identifier

        if infant_alive == NO:
            self.eligible = False
            self.reasons_ineligible = 'Infant is not alive'

        if infant_weight == NO:
            self.eligible = False
            self.reasons_ineligible = 'Infant weight < 2.00 kilograms'

        if major_anomalies == YES:
            self.eligible = False
            self.reasons_ineligible = 'Infant was born with major'
            ' congenital anomalies'

        if birth_complications == YES:
            self.eligible = False
            self.reasons_ineligible = 'Infant experienced birth complications'

        if infant_documentation == NO:
            self.eligible = False
            self.reasons_ineligible = 'Infant does not have documentation that'
            ' they received a BCG vaccine within 72 hours of birth'
            ' in the Under 5 Health'

        if infant_months == YES or not self.validate_infant_weight():
            self.eligible = False
            self.reasons_ineligible = 'Infant has reached 14 months of age '

        if tb_treatment == NO:
            self.eligible = False
            self.reasons_ineligible = 'Woman was not being in tb treatment'
            ' during pregnancy'

        if incarcerated == NO:
            self.eligible = False
            self.reasons_ineligible = 'Woman is not incarcernated'

        if willing_to_consent == NO:
            self.eligible = False
            self.reasons_ineligible = 'Woman is not willing to provide'
            ' informed consent'

    def validate_infant_weight(self):
        infant_birth_data = self.infant_birth_data_cls.objects.get(
            subject_identifier=self.subject_identifier)

        if infant_birth_data:
            weight = infant_birth_data.weight_kg
            if int(weight) >= 2:
                return True
        return False

    @property
    def infant_birth_data_cls(self):
        return django_apps.get_model(self.infant_bith_data)

    def infant_birth_months(self):
        ''' checks if the infant reached 14 months of age or has the infant already
            attended the 12 month Tshilo Dikotla Study visit
        '''
