from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from Company.models import User , Employee

@receiver(post_save, sender=User)
def createEmployee(sender, instance, created, **kwargs):
    user = instance
    Employee.objects.create(user=user,username=user.username)