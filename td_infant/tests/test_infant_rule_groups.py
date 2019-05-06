from django.test import tag
from edc_appointment.models import Appointment as MaternalAppointment
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata, RequisitionMetadata
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from td_maternal.tests.base_test_case import BaseTestCase

from ..models import Appointment


@tag('infant')
class TestInfantRules(BaseTestCase):

    def setUp(self):
        super(TestInfantRules, self).setUp()
        self.create_mother(self.hiv_pos_mother_options())
        appointment_1020 = MaternalAppointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_1020)
        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow())

        self.infant_reg_subject = RegisteredSubject.objects.get(
            relative_identifier=self.subject_consent.subject_identifier)
        mommy.make_recipe(
            'td_infant.infantbirth',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow())

    def test_infant_congenital_anomalies_not_required(self):
        appointment_2000 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2000')

        infant_visit = mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)

        mommy.make_recipe(
            'td_infant.infantbirthdata',
            infant_visit=infant_visit,
            congenital_anomalities=NO)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_infant.infantcongenitalanomalies',
                subject_identifier=appointment_2000.subject_identifier,
                visit_code='2000').entry_status, NOT_REQUIRED)

    def test_infant_congenital_anomalies_required(self):
        appointment_2000 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2000')

        infant_visit = mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)

        mommy.make_recipe(
            'td_infant.infantbirthdata',
            infant_visit=infant_visit,
            congenital_anomalities=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_infant.infantcongenitalanomalies',
                subject_identifier=appointment_2000.subject_identifier,
                visit_code='2000').entry_status, REQUIRED)

    def test_infant_birth_arv_required(self):
        appointment_2000 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2000')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_infant.infantbirtharv',
                subject_identifier=appointment_2000.subject_identifier,
                visit_code='2000').entry_status, REQUIRED)

    def test_infant_birth_arv_not_required(self):
        super(TestInfantRules, self).setUp()
        self.create_mother(self.hiv_neg_mother_options())
        appointment_1020 = MaternalAppointment.objects.get(
            subject_identifier=self.subject_consent.subject_identifier,
            visit_code='1020M')

        mommy.make_recipe(
            'td_maternal.maternalvisit',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_1020)
        mommy.make_recipe(
            'td_maternal.maternallabourdel',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow())

        self.infant_reg_subject = RegisteredSubject.objects.get(
            relative_identifier=self.subject_consent.subject_identifier)
        mommy.make_recipe(
            'td_infant.infantbirth',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow())

        appointment_2000 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2000')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_infant.infantbirtharv',
                subject_identifier=appointment_2000.subject_identifier,
                visit_code='2000').entry_status, NOT_REQUIRED)

    def test_infant_dna_pcr_required(self):

        appointment_2000 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2000')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)

        appointment_2010 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2010')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2010)

        appointment_2020 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2020')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2020)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='td_infant.infantrequisition',
                panel_name='dna_pcr',
                subject_identifier=appointment_2000.subject_identifier,
                visit_code='2020').entry_status, REQUIRED)

    @tag('rr')
    def test_infant_infant_elisa_required(self):

        appointment_2000 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2000')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)

        appointment_2010 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2010')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2010)

        appointment_2020 = Appointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2020')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2020)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='td_infant.infantrequisition',
                panel_name='infant_elisa',
                subject_identifier=appointment_2000.subject_identifier,
                visit_code='2020').entry_status, NOT_REQUIRED)
