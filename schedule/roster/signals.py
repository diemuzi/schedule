from roster import models


def create_roster(sender, instance, created, **kwargs):
    if created:
        models.Roster.objects.create(account=instance)
