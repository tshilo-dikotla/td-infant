from django.test import tag
from edc_appointment.models import Appointment as MaternalAppointment
from edc_base.utils import get_utcnow
from edc_constants.constants import INCOMPLETE
from edc_metadata.constants import REQUIRED
from edc_metadata.models import CrfMetadata
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from td_maternal.tests.base_test_case import BaseTestCase

from ..models import Appointment as InfantAppointment


@tag('karabo')
class TestKaraboConsentSave(BaseTestCase):

    def setUp(self):
        super(TestKaraboConsentSave, self).setUp()
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

    def test_karabo_tb_form_required(self):
        appointment_2000 = InfantAppointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2000')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2000)
        appointment_2000.appt_status = INCOMPLETE
        appointment_2000.save()

        mommy.make_recipe(
            'td_infant.karabosubjectscreening',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow())

        mommy.make_recipe(
            'td_infant.karabosubjectconsent',
            subject_identifier=self.subject_consent.subject_identifier,
            report_datetime=get_utcnow())

        appointment_2010 = InfantAppointment.objects.get(
            subject_identifier=self.infant_reg_subject.subject_identifier,
            visit_code='2010')

        mommy.make_recipe(
            'td_infant.infantvisit',
            subject_identifier=self.infant_reg_subject.subject_identifier,
            report_datetime=get_utcnow(),
            appointment=appointment_2010)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='td_infant.karabotuberculosishistory',
                subject_identifier=self.infant_reg_subject.subject_identifier,
                visit_code='2010').entry_status, REQUIRED)
