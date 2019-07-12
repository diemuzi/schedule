from django import forms

from schedule.roster import models


class FormEdit(forms.ModelForm):
    class Meta:
        model = models.Roster

        fields = [
            'is_sunday',
            'has_break_sunday',
            'sunday_start_time_counter',
            'sunday_end_time_counter',
            'sunday_start_time_outside',
            'sunday_end_time_outside',
            'is_monday',
            'has_break_monday',
            'monday_start_time_counter',
            'monday_end_time_counter',
            'monday_start_time_outside',
            'monday_end_time_outside',
            'is_tuesday',
            'has_break_tuesday',
            'tuesday_start_time_counter',
            'tuesday_end_time_counter',
            'tuesday_start_time_outside',
            'tuesday_end_time_outside',
            'is_wednesday',
            'has_break_wednesday',
            'wednesday_start_time_counter',
            'wednesday_end_time_counter',
            'wednesday_start_time_outside',
            'wednesday_end_time_outside',
            'is_thursday',
            'has_break_thursday',
            'thursday_start_time_counter',
            'thursday_end_time_counter',
            'thursday_start_time_outside',
            'thursday_end_time_outside',
            'is_friday',
            'has_break_friday',
            'friday_start_time_counter',
            'friday_end_time_counter',
            'friday_start_time_outside',
            'friday_end_time_outside',
            'is_saturday',
            'has_break_saturday',
            'saturday_start_time_counter',
            'saturday_end_time_counter',
            'saturday_start_time_outside',
            'saturday_end_time_outside'
        ]
