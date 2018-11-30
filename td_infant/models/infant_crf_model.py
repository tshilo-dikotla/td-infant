from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_offstudy.models import OffStudyMixin
from .model_mixins import CrfModelMixin
from ..managers import InfantVisitCrfManager
from .infant_visit import InfantVisit
from edc_meta_data.managers import CrfMetaDataManager



class InfantCrfModel(CrfModelMixin, OffStudyMixin,
                    BaseUuidModel):

    """ A model completed by the user on the infant's scheduled visit. """

    off_study_model = ('td_infant', 'InfantOffStudy')

    infant_visit = models.OneToOneField(InfantVisit)

    objects = InfantVisitCrfManager()
    entry_meta_data_manager = CrfMetaDataManager(InfantVisit)

    def __str__(self):
        return "{}: {}".format(self.__class__._meta.model_name,
                               self.infant_visit.appointment.registered_subject.subject_identifier)

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.get_visit().appointment.registered_subject.relative_identifier

    class Meta:
        abstract = True
