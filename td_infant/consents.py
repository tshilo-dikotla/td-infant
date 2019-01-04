from datetime import datetime

import arrow
from dateutil.tz import gettz
from django.apps import apps as django_apps
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE


app_config = django_apps.get_app_config('edc_protocol')
edc_protocol = django_apps.get_app_config('edc_protocol')

tzinfo = gettz('Africa/Gaborone')

v3 = Consent(
    'td_infant.infantdummysubjectconsent',
    version='3',
    start=arrow.get(
        datetime(2018, 2, 1, 0, 0, 0), tzinfo=tzinfo).to('UTC').datetime,
    end=arrow.get(
        datetime(2020, 11, 30, 23, 59, 59), tzinfo=tzinfo).to('UTC').datetime,
    age_min=1,
    age_is_adult=1,
    age_max=10,
    gender=[MALE, FEMALE])

site_consents.register(v3)
