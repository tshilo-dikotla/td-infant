from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class TestCode (ListModelMixin, BaseUuidModel):

    pass


class AutopsyInfoSource(ListModelMixin, BaseUuidModel):

    pass


class ChronicConditions(ListModelMixin, BaseUuidModel):

    pass


class Contraceptives(ListModelMixin, BaseUuidModel):

    pass


class CovidSymptoms (ListModelMixin, BaseUuidModel):

    pass


class DeliveryComplications(ListModelMixin, BaseUuidModel):

    pass


class DiseasesAtEnrollment (ListModelMixin, BaseUuidModel):

    pass


class Foods (ListModelMixin, BaseUuidModel):

    pass


class HouseholdGoods (ListModelMixin, BaseUuidModel):

    pass


class Malformations(ListModelMixin, BaseUuidModel):

    pass


class MaternalDiagnosesList(ListModelMixin, BaseUuidModel):

    pass


class MaternalMedications(ListModelMixin, BaseUuidModel):

    pass


class MaternalHospitalization(ListModelMixin, BaseUuidModel):

    pass


class HealthCond (ListModelMixin, BaseUuidModel):

    pass


class DelComp (ListModelMixin):

    pass


class ObComp(ListModelMixin):

    pass


class MaternalRelatives(ListModelMixin, BaseUuidModel):

    pass


class PriorArv (ListModelMixin, BaseUuidModel):

    pass


class RandomizationItem (ListModelMixin, BaseUuidModel):

    pass


class Rations (ListModelMixin, BaseUuidModel):

    pass


class Supplements (ListModelMixin, BaseUuidModel):

    pass


class WcsDxAdult(ListModelMixin, BaseUuidModel):

    pass


class WcsDxPed(ListModelMixin, BaseUuidModel):

    pass


class CoughingRelation(ListModelMixin, BaseUuidModel):
    pass


class FeverRelation(ListModelMixin, BaseUuidModel):
    pass


class WeightLossRelation(ListModelMixin, BaseUuidModel):
    pass


class NightSweatsRelation(ListModelMixin, BaseUuidModel):
    pass


class DiagnosisRelation(ListModelMixin, BaseUuidModel):
    pass
