from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_offstudy.model_mixins import OffstudyModelMixin
from .model_mixins import CrfModelMixin
from .infant_visit import InfantVisit
# from edc_metadata.managers import CrfMetadataManager
from django.db.models.deletion import PROTECT


class InfantCrfModel(CrfModelMixin, OffstudyModelMixin,
                     BaseUuidModel):

    """ A model completed by the user on the infant's scheduled visit. """

    infant_visit = models.OneToOneField(InfantVisit, on_delete=PROTECT)

#     entry_meta_data_manager = CrfMetadataManager(InfantVisit)

    def __str__(self):
        return "{}: {}".format(self.__class__._meta.model_name,
                               self.infant_visit.appointment.registered_subject.subject_identifier)

    def get_consenting_subject_identifier(self):
        """Returns mother's identifier."""
        return self.get_visit().appointment.registered_subject.relative_identifier

    class Meta:
        abstract = True
