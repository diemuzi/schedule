from django import forms
from django.contrib.auth import get_user_model

from roster import models


class FormProfile(forms.ModelForm):
    class Meta:
        model = get_user_model()

        fields = [
            'first_name',
            'last_name',
            'facility'
        ]


class FormSchedule(forms.ModelForm):
    class Meta:
        model = models.Roster

        fields = [
            'is_sunday',
            'has_break_sunday',
            'start_time_sunday',
            'end_time_sunday',
            'is_monday',
            'has_break_monday',
            'start_time_monday',
            'end_time_monday',
            'is_tuesday',
            'has_break_tuesday',
            'start_time_tuesday',
            'end_time_tuesday',
            'is_wednesday',
            'has_break_wednesday',
            'start_time_wednesday',
            'end_time_wednesday',
            'is_thursday',
            'has_break_thursday',
            'start_time_thursday',
            'end_time_thursday',
            'is_friday',
            'has_break_friday',
            'start_time_friday',
            'end_time_friday',
            'is_saturday',
            'has_break_saturday',
            'start_time_saturday',
            'end_time_saturday'
        ]
