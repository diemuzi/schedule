from django.conf import settings
from django.core import validators
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

    def profile(self):
        return Roster.objects.get(pk=self)

    @staticmethod
    def search_staff():
        return Roster.objects.filter(account__is_staff=True, account__is_superuser=False)
