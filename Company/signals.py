from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from .models import Manager , User , Employee

#Thos is used for creating a manager object when I am creating a User instance in register.html
#Signals are very useful for this type of use case. It can also be used to update user instance along with manager instance/
@receiver(post_save, sender=User)
def createManager(sender, instance, created, **kwargs):
    if created:
        user = instance
        Manager.objects.create(user=user,username=user.username)

