from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from .models import Manager , User , Employee


@receiver(post_save, sender=User)
def createManager(sender, instance, created, **kwargs):
    if created:
        user = instance
        Manager.objects.create(user=user,username=user.username)

