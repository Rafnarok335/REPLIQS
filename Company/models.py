from django.db import models
from django.conf import settings
# Create your models here.
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser



# This is an abstract class that is inherited by the User class. I am using this to differentiate between the two types of users and their usecases.
class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

## This is the employee table where i store the employee details with the fields here. I kept field here minimum.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='employee')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    date_of_joining = models.DateField()
    def __str__(self):
        return self.user.username

# This is the manager of an individual who represents their company and handles the assets.
class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='manager')
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()
    
    company = models.CharField(max_length=100)
    def __str__(self):  
        return self.user.username


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['name','username','email','phone','address','department','salary','company']


        def __init__(self, *args, **kwargs):
            super(ManagerForm, self).__init__(*args, **kwargs)