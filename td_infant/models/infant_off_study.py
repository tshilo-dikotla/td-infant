from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_export.model_mixins import ExportTrackingFieldsModelMixin
# from edc_metadata.managers import CrfMetadataManager
from edc_offstudy.model_mixins import OffstudyModelMixin
from edc_visit_tracking.model_mixins import CrfModelMixin

from .infant_visit import InfantVisit


class InfantOffStudy(CrfModelMixin, OffstudyModelMixin,
                     ExportTrackingFieldsModelMixin, BaseUuidModel):

    """ A model completed by the user when the infant is taken off study. """

    infant_visit = models.OneToOneField(InfantVisit, on_delete=PROTECT)

#     entry_meta_data_manager = CrfMetadataManager(InfantVisit)

    class Meta:
        app_label = 'td_infant'
        verbose_name = "Infant Off-Study"
        verbose_name_plural = "Infant Off-Study"
