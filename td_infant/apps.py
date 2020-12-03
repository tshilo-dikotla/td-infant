from django.apps import AppConfig as DjangoApponfig
from django.conf import settings


class AppConfig(DjangoApponfig):
    name = 'td_infant'
    verbose_name = 'Tshilo Dikotla Infant CRFs'
    admin_site_name = 'td_infant_admin'

    def ready(self):
        from .models import infant_birth_on_post_save
        from .models import resave_infant_visit_on_post_save


if settings.APP_NAME == 'td_infant':
    from datetime import datetime
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
    from dateutil.tz import gettz
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_constants.constants import FAILED_ELIGIBILITY
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_visit_tracking.constants import MISSED_VISIT
    from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
    from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
    from edc_timepoint.timepoint_collection import TimepointCollection
    from edc_timepoint.timepoint import Timepoint
    from edc_appointment.constants import COMPLETE_APPT

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'td_infant': ('infant_visit', 'td_infant.infantvisit'),
            'td_maternal': ('maternal_visit', 'td_maternal.maternalvisit')}

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP085'
        protocol_number = '085'
        protocol_name = 'Tshilo Dikotla'
        protocol_title = ''
        study_open_datetime = datetime(
            2016, 4, 1, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2022, 5, 31, 23, 59, 59, tzinfo=gettz('UTC'))

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='td_maternal.maternalvisit'),
            AppointmentConfig(
                model='td_infant.appointment',
                related_visit_model='td_infant.infantvisit')
        ]

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'td_infant.infantvisit': 'reason',
                        'td_maternal.maternalvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY, MISSED_VISIT]

    class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
        timepoints = TimepointCollection(
            timepoints=[
                Timepoint(
                    model='td_infant.appointment',
                    datetime_field='appt_datetime',
                    status_field='appt_status',
                    closed_status=COMPLETE_APPT),
                Timepoint(
                    model='td_infant.historicalappointment',
                    datetime_field='appt_datetime',
                    status_field='appt_status',
                    closed_status=COMPLETE_APPT),
                Timepoint(
                    model='edc_appointment.appointment',
                    datetime_field='appt_datetime',
                    status_field='appt_status',
                    closed_status=COMPLETE_APPT),
                Timepoint(
                    model='edc_appointment.historicalappointment',
                    datetime_field='appt_datetime',
                    status_field='appt_status',
                    closed_status=COMPLETE_APPT)
            ])

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}
