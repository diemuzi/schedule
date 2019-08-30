import pytz
from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker

FACILITY_CHOICES = (
    ('bgm', _('BGM')),
    ('scm', _('SCM'))
)

FORM_DISPLAY_CHOICES = (
    ('compact', _('Compact')),
    ('expand', _('Expanded'))
)

HELP_TEXT_CHOICES = (
    (False, _('No')),
    (True, _('Yes'))
)

LOCALE_CHOICES = (
    ('en', _('English')),
    ('de', _('German'))
)

TIME_FORMAT_CHOICES = (
    ('l, F d, Y g:i:s A', 'Sunday, January 01, 2000 1:00:00 PM'),
    ('l, F d, Y H:i:s', 'Sunday, January 01, 2000 13:00:00'),
    ('F d, Y g:i:s A', 'January 01, 2000 1:00:00 PM'),
    ('F d, Y H:i:s', 'January 01, 2000 13:00:00'),
    ('Y-m-d g:i:s A', '2000-01-01 1:00:00 PM'),
    ('Y-m-d H:i:s', '2000-01-01 13:00:00')
)

TIME_ZONE_CHOICES = (
    sorted([(x, x) for x in pytz.all_timezones_set])
)


class Account(auth_models.AbstractUser):
    date_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On')
    )

    email = models.EmailField(
        validators=[
            validators.MinLengthValidator(5),
            validators.EmailValidator
        ],
        verbose_name=_('Email Address'),
        blank=False,
        null=False,
        help_text=_('Email address for any notifications.')
    )

    first_name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ],
        verbose_name=_('First Name'),
        blank=False,
        null=False,
        help_text=_('Your legal first name.')
    )

    form_display = models.CharField(
        max_length=7,
        choices=FORM_DISPLAY_CHOICES,
        default='expand',
        verbose_name=_('Form Display'),
        blank=False,
        null=False,
        help_text=_('Choose how forms should be displayed.')
    )

    help_text = models.BooleanField(
        choices=HELP_TEXT_CHOICES,
        default=True,
        verbose_name=_('Help Text'),
        help_text=_('Choose if help text should be displayed.')
    )

    last_name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ],
        verbose_name=_('Last Name'),
        blank=False,
        null=False,
        help_text=_('Your legal last name.')
    )

    locale = models.CharField(
        max_length=2,
        choices=LOCALE_CHOICES,
        default='en',
        verbose_name=_('Language'),
        blank=False,
        null=False,
        help_text=_('Choose a default language.')
    )

    time_format = models.CharField(
        max_length=255,
        choices=TIME_FORMAT_CHOICES,
        default='Y-m-d H:i:s',
        verbose_name=_('Time Format'),
        blank=False,
        null=False,
        help_text=_('Choose a preferred time format.')
    )

    time_zone = models.CharField(
        max_length=32,
        choices=TIME_ZONE_CHOICES,
        default='US/Central',
        verbose_name=_('Time Zone'),
        blank=False,
        null=False,
        help_text=_('Choose a preferred time zone.')
    )

    facility = models.CharField(
        max_length=3,
        choices=FACILITY_CHOICES,
        default='scm',
        blank=False,
        null=False,
        verbose_name=_('Facility'),
        help_text=_('Choose a location.')
    )

    tracker = FieldTracker()

    class Meta:
        db_table = 'account'

        default_permissions = ()

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Roster(models.Model):
    account = models.OneToOneField(
        Account,
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

        default_permissions = ()
