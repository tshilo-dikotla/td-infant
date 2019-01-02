from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_base.sites import CurrentSiteManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin


class OnScheduleInfantBirth(OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by infant birth.
    """
    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def put_on_schedule(self):
        pass
