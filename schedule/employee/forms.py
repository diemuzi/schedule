from django import forms
from django.contrib.auth.hashers import get_random_string
from django.contrib.auth.hashers import make_password

from schedule.employee import models


class FormAdd(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'first_name',
            'last_name',
            'facility'
        ]

    def save(self, commit=True):
        self.instance.email = 'none@example.com'
        self.instance.username = get_random_string()
        self.instance.password = make_password(get_random_string())
        self.instance.is_active = True
        self.instance.is_staff = True

        return super(FormAdd, self).save()


class FormEdit(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'first_name',
            'last_name',
            'facility'
        ]
