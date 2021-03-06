from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, MALE, ALIVE, ON_STUDY, NO
from edc_visit_tracking.constants import SCHEDULED
from faker import Faker
from model_mommy.recipe import Recipe, seq

from .models import InfantBirth, InfantVisit, InfantBirthData


fake = Faker()

infantbirth = Recipe(
    InfantBirth,
    report_datetime=get_utcnow(),
    first_name=fake.first_name,
    initials='AA',
    dob=get_utcnow().date(),
    gender=MALE,
    site=Site.objects.get_current(),
)

infantbirthdata = Recipe(
    InfantBirthData,
    infant_gender=MALE,
    weight_kg=2,
    infant_length=45.0,
    head_circumference=20.0,
    apgar_score=YES,
    apgar_score_min_1=7,
    apgar_score_min_5=8,
    apgar_score_min_10=9,
    congenital_anomalities=NO
)

# karabosubjectconsent = Recipe(
#     KaraboSubjectConsent,
#     report_datetime=get_utcnow(),
#     first_name=fake.first_name,
#     last_name=fake.last_name,
#     initials='XX',
#     language='en',
#     is_literate=YES,
#     consent_datetime=get_utcnow(),
#     identity=seq('212323231', increment_by=1),
#     consent_reviewed=YES,
#     study_questions=YES,
#     assessment_score=YES,
#     consent_signature=YES,
#     consent_copy=YES,
#     site=Site.objects.get_current(),
# )

infantvisit = Recipe(
    InfantVisit,
    report_datetime=get_utcnow(),
    reason=SCHEDULED,
    study_status=ON_STUDY,
    survival_status=ALIVE,
    info_source='MOTHER')

# karabosubjectscreening = Recipe(
#     KaraboSubjectScreening,
#     report_datetime=get_utcnow(),
#     infant_alive=YES,
#     infant_weight=YES,
#     major_anomalies=NO,
#     birth_complications=NO,
#     infant_documentation=YES,
#     infant_months=YES,
#     tb_treatment=YES,
#     incarcerated=NO,
#     willing_to_consent=YES
# )
