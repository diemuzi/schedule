from django.db.models.signals import post_save
from django.dispatch import receiver

from schedule.employee import models


@receiver(post_save, sender=models.Account)
def account_roster_create(sender, instance, created, **kwargs):
    if created:
        models.Roster.objects.create(account=instance)
