from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from ..admin_site import td_infant_admin
from ..constants import INFANT
from ..forms import (
    InfantCongenitalAnomaliesForm, InfantFacialDefectForm,
    InfantCleftDisorderForm, InfantMouthUpGiForm,
    InfantCardioDisorderForm,
    InfantRespiratoryDefectForm, InfantLowerGiForm,
    InfantFemaleGenitalForm,
    InfantMaleGenitalForm, InfantRenalForm,
    InfantMusculoskeletalForm,
    InfantSkinForm, InfantTrisomiesForm,
    InfantCnsForm
)
from ..models import (
    InfantCongenitalAnomalies, InfantCns, InfantFacialDefect,
    InfantCleftDisorder, InfantMouthUpGi, InfantCardioDisorder,
    InfantRespiratoryDefect, InfantLowerGi, InfantMaleGenital,
    InfantFemaleGenital, InfantRenal, InfantMusculoskeletal,
    InfantSkin, InfantTrisomies
)
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(InfantCns, site=td_infant_admin)
class InfantCnsAdmin(CrfModelAdminMixin):
    form = InfantCnsForm
    list_display = ('congenital_anomalies', 'abnormality_status',)

    list_filter = ('cns',)

    radio_fields = {
        'cns': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantCnsInline(TabularInlineMixin, admin.TabularInline):

    model = InfantCns
    form = InfantCnsForm
    extra = 0


@admin.register(InfantFacialDefect, site=td_infant_admin)
class InfantFacialDefectAdmin(CrfModelAdminMixin):
    form = InfantFacialDefectForm
    list_display = ('congenital_anomalies',)

    radio_fields = {
        'facial_defect': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]


class InfantFacialDefectInline(TabularInlineMixin, admin.TabularInline):

    model = InfantFacialDefect
    form = InfantFacialDefectForm
    extra = 0


@admin.register(InfantCleftDisorder, site=td_infant_admin)
class InfantCleftDisorderAdmin(CrfModelAdminMixin):
    form = InfantCleftDisorderForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'cleft_disorder': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantCleftDisorderInline(TabularInlineMixin, admin.TabularInline):

    model = InfantCleftDisorder
    form = InfantCleftDisorderForm
    extra = 0


@admin.register(InfantMouthUpGi, site=td_infant_admin)
class InfantMouthUpGiAdmin(CrfModelAdminMixin):
    form = InfantMouthUpGiForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'mouth_up_gi': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantMouthUpGiInline(TabularInlineMixin, admin.TabularInline):

    model = InfantMouthUpGi
    form = InfantMouthUpGiForm
    extra = 0


@admin.register(InfantCardioDisorder, site=td_infant_admin)
class InfantCardioDisorderAdmin(CrfModelAdminMixin):
    form = InfantCardioDisorderForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'cardio_disorder': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantCardioDisorderInline(TabularInlineMixin, admin.TabularInline):

    model = InfantCardioDisorder
    form = InfantCardioDisorderForm
    extra = 0


@admin.register(InfantRespiratoryDefect, site=td_infant_admin)
class InfantRespiratoryDefectAdmin(CrfModelAdminMixin):
    form = InfantRespiratoryDefectForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'respiratory_defect': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantRespiratoryDefectInline(TabularInlineMixin, admin.TabularInline):

    model = InfantRespiratoryDefect
    form = InfantRespiratoryDefectForm
    extra = 0


@admin.register(InfantLowerGi, site=td_infant_admin)
class InfantLowerGiAdmin(CrfModelAdminMixin):
    form = InfantLowerGiForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'lower_gi': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantLowerGiInline(TabularInlineMixin, admin.TabularInline):

    model = InfantLowerGi
    form = InfantLowerGiForm
    extra = 0


@admin.register(InfantFemaleGenital, site=td_infant_admin)
class InfantFemaleGenitalAdmin(CrfModelAdminMixin):
    form = InfantFemaleGenitalForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'female_genital': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantFemaleGenitalInline(TabularInlineMixin, admin.TabularInline):

    model = InfantFemaleGenital
    form = InfantFemaleGenitalForm
    extra = 0


@admin.register(InfantMaleGenital, site=td_infant_admin)
class InfantMaleGenitalAdmin(CrfModelAdminMixin):
    form = InfantMaleGenitalForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'male_genital': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantMaleGenitalInline(TabularInlineMixin, admin.TabularInline):

    model = InfantMaleGenital
    form = InfantMaleGenitalForm
    extra = 0


@admin.register(InfantRenal, site=td_infant_admin)
class InfantRenalAdmin(CrfModelAdminMixin):
    form = form = InfantRenalForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'renal': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantRenalInline(TabularInlineMixin, admin.TabularInline):

    model = InfantRenal
    form = InfantRenalForm
    extra = 0


@admin.register(InfantMusculoskeletal, site=td_infant_admin)
class InfantMusculoskeletalAdmin(CrfModelAdminMixin):
    form = form = InfantMusculoskeletalForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'musculo_skeletal': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantMusculoskeletalInline(TabularInlineMixin, admin.TabularInline):

    model = InfantMusculoskeletal
    form = InfantMusculoskeletalForm
    extra = 0


@admin.register(InfantSkin, site=td_infant_admin)
class InfantSkinAdmin(CrfModelAdminMixin):
    form = form = InfantSkinForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'skin': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantSkinInline(TabularInlineMixin, admin.TabularInline):

    model = InfantSkin
    form = InfantSkinForm
    extra = 0


@admin.register(InfantTrisomies, site=td_infant_admin)
class InfantTrisomiesAdmin(CrfModelAdminMixin):
    form = InfantTrisomiesForm

    list_display = ('congenital_anomalies',)

    search_fields = [
        'congenital_anomalies__infant_visit__appointment__registered_subject__subject_identifier',
        'congenital_anomalies__infant_visit__appointment__registered_subject__initials', ]

    radio_fields = {
        'trisomies': admin.VERTICAL,
        'abnormality_status': admin.VERTICAL
    }


class InfantTrisomiesInline(TabularInlineMixin, admin.TabularInline):

    model = InfantTrisomies
    form = InfantTrisomiesForm
    extra = 0


@admin.register(InfantCongenitalAnomalies, site=td_infant_admin)
class InfantCongenitalAnomaliesAdmin(CrfModelAdminMixin):

    form = InfantCongenitalAnomaliesForm
    dashboard_type = INFANT
    visit_model_name = 'infantvisit'

    list_display = ('infant_visit',)

    inlines = [
        InfantCnsInline,
        InfantFacialDefectInline,
        InfantCleftDisorderInline,
        InfantMouthUpGiInline,
        InfantCardioDisorderInline,
        InfantRespiratoryDefectInline,
        InfantLowerGiInline,
        InfantFemaleGenitalInline,
        InfantMaleGenitalInline,
        InfantRenalInline,
        InfantMusculoskeletalInline,
        InfantSkinInline,
        InfantTrisomiesInline]
