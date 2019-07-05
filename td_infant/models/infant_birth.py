from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django_crypto_fields.fields import EncryptedCharField
from django_crypto_fields.fields import FirstnameField
from django_crypto_fields.mixins import CryptoMixin
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.model_validators.date import date_not_future
from edc_base.sites import SiteModelMixin
from edc_constants.choices import GENDER_UNDETERMINED
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugModelMixin


class InfantBirth(UniqueSubjectIdentifierFieldMixin, SiteModelMixin,
                  SearchSlugModelMixin, CryptoMixin, BaseUuidModel):
    """ A model completed by the user on the infant's birth. """

    report_datetime = models.DateTimeField(
        verbose_name="Date and Time infant enrolled",
        validators=[
            datetime_not_future, ],
        help_text='')

    first_name = FirstnameField(
        max_length=25,
        verbose_name="Infant's first name",
        help_text="If infant name is unknown or not yet determined, "
                  "use Baby + birth order + mother's last name, e.g. 'Baby1Malane'")

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.'))],)

    dob = models.DateField(
        verbose_name='Date of Birth',
        help_text="Must match labour and delivery report.",
        validators=[date_not_future, ])

    gender = models.CharField(
        max_length=10,
        choices=GENDER_UNDETERMINED)

    def __str__(self):
        return f'{self.first_name}, {self.initials}, {self.gender}'

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(InfantBirth, self).save(*args, **kwargs)

    def get_consent_version(self):
        subject_consent_cls = django_apps.get_model(
            'td_infant.infantdummysubjectconsent')
        subject_consent_objs = subject_consent_cls.objects.filter(
            subject_identifier=self.subject_identifier).order_by(
                '-consent_datetime')
        if subject_consent_objs:
            return subject_consent_objs.first().version
        else:
            raise ValidationError(
                'Missing Infant Dummy Consent form. Cannot proceed.')

    @property
    def schedule_name(self):
        """Return a visit schedule name.
        """
        schedule_name = None
        subject_consent = django_apps.get_model(
            'td_maternal.subjectconsent').objects.filter(
                subject_identifier=self.registered_subject.relative_identifier).order_by('version').last()
        if subject_consent.version == '1':
            schedule_name = 'infant_schedule_v1'
        elif subject_consent.version == '3':
            schedule_name = 'infant_schedule_v3'
        return schedule_name

    @property
    def registered_subject(self):
        """Return infant registered subject.
        """
        registered_subject_cls = django_apps.get_model(
            'edc_registration.registeredsubject')
        try:
            registered_subject = registered_subject_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except registered_subject_cls.DoesNotExist:
            raise ValidationError(
                f'Registered Subject is missing for {self.subject_identifier}')
        else:
            return registered_subject

    class Meta:
        app_label = 'td_infant'
        verbose_name = "Infant Birth"
