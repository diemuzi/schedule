from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker


class Roster(models.Model):
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='roster_account',
        on_delete=models.CASCADE,
        primary_key=True
    )

    is_sunday = models.BooleanField(
        default=False,
        verbose_name=_('Sunday')
    )

    has_break_sunday = models.BooleanField(
        default=False,
        verbose_name=_('Break')
    )

    start_time_sunday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('Start Time')
    )

    end_time_sunday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('End Time')
    )

    is_monday = models.BooleanField(
        default=False,
        verbose_name=_('Monday')
    )

    has_break_monday = models.BooleanField(
        default=False,
        verbose_name=_('Break')
    )

    start_time_monday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('Start Time')
    )

    end_time_monday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('End Time')
    )

    is_tuesday = models.BooleanField(
        default=False,
        verbose_name=_('Tuesday')
    )

    has_break_tuesday = models.BooleanField(
        default=False,
        verbose_name=_('Break')
    )

    start_time_tuesday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('Start Time')
    )

    end_time_tuesday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('End Time')
    )

    is_wednesday = models.BooleanField(
        default=False,
        verbose_name=_('Wednesday')
    )

    has_break_wednesday = models.BooleanField(
        default=False,
        verbose_name=_('Break')
    )

    start_time_wednesday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('Start Time')
    )

    end_time_wednesday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('End Time')
    )

    is_thursday = models.BooleanField(
        default=False,
        verbose_name=_('Thursday')
    )

    has_break_thursday = models.BooleanField(
        default=False,
        verbose_name=_('Break')
    )

    start_time_thursday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('Start Time')
    )

    end_time_thursday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('End Time')
    )

    is_friday = models.BooleanField(
        default=False,
        verbose_name=_('Friday')
    )

    has_break_friday = models.BooleanField(
        default=False,
        verbose_name=_('Break')
    )

    start_time_friday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('Start Time')
    )

    end_time_friday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('End Time')
    )

    is_saturday = models.BooleanField(
        default=False,
        verbose_name=_('Saturday')
    )

    has_break_saturday = models.BooleanField(
        default=False,
        verbose_name=_('Break')
    )

    start_time_saturday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('Start Time')
    )

    end_time_saturday = models.CharField(
        max_length=4,
        validators=[
            validators.RegexValidator('^[0-9]+$')
        ],
        blank=True,
        null=True,
        verbose_name=_('End Time')
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'roster'

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        error = {}

        is_day = {
            'sunday': self.is_sunday,
            'monday': self.is_monday,
            'tuesday': self.is_tuesday,
            'wednesday': self.is_wednesday,
            'thursday': self.is_thursday,
            'friday': self.is_friday,
            'saturday': self.is_saturday
        }

        validation_error = _('Value must be set.')

        for key, value in is_day.items():
            # Sunday
            if value is True and key == 'sunday':
                if self.start_time_sunday is None:
                    error['start_time_sunday'] = ValidationError(validation_error, code='invalid')

                if self.end_time_sunday is None:
                    error['end_time_sunday'] = ValidationError(validation_error, code='invalid')

            # Monday
            if value is True and key == 'monday':
                if self.start_time_monday is None:
                    error['start_time_monday'] = ValidationError(validation_error, code='invalid')

                if self.end_time_monday is None:
                    error['end_time_monday'] = ValidationError(validation_error, code='invalid')

            # Tuesday
            if value is True and key == 'tuesday':
                if self.start_time_tuesday is None:
                    error['start_time_tuesday'] = ValidationError(validation_error, code='invalid')

                if self.end_time_tuesday is None:
                    error['end_time_tuesday'] = ValidationError(validation_error, code='invalid')

            # Wednesday
            if value is True and key == 'wednesday':
                if self.start_time_wednesday is None:
                    error['start_time_wednesday'] = ValidationError(validation_error, code='invalid')

                if self.end_time_wednesday is None:
                    error['end_time_wednesday'] = ValidationError(validation_error, code='invalid')

            # Thursday
            if value is True and key == 'thursday':
                if self.start_time_thursday is None:
                    error['start_time_thursday'] = ValidationError(validation_error, code='invalid')

                if self.end_time_thursday is None:
                    error['end_time_thursday'] = ValidationError(validation_error, code='invalid')

            # Friday
            if value is True and key == 'friday':
                if self.start_time_friday is None:
                    error['start_time_friday'] = ValidationError(validation_error, code='invalid')

                if self.end_time_friday is None:
                    error['end_time_friday'] = ValidationError(validation_error, code='invalid')

            # Saturday
            if value is True and key == 'saturday':
                if self.start_time_saturday is None:
                    error['start_time_saturday'] = ValidationError(validation_error, code='invalid')

                if self.end_time_saturday is None:
                    error['end_time_saturday'] = ValidationError(validation_error, code='invalid')

        if error:
            raise ValidationError(error)

    def profile(self):
        return Roster.objects.get(pk=self)

    @staticmethod
    def search_staff():
        return Roster.objects.filter(account__is_staff=True, account__is_superuser=False)
