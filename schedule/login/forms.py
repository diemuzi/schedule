from django import forms

from login import models


class FormCreate(forms.ModelForm):
    class Meta:
        model = models.Account

        fields = [
            'email',
            'first_name',
            'last_name'
        ]

    def save(self, commit=True):
        instance = super(FormCreate, self).save(commit=False)

        instance.create_account()

        return instance
