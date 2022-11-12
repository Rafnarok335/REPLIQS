from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employess(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.ForeignKey(User, on_delete=models.CASCADE, max_length=30)
    emp_email = models.EmailField(max_length=30)
    emp_address = models.CharField(max_length=30)
    emp_salary = models.IntegerField()
    emp_dob = models.DateField()
    Phone = models.DecimalField(("Phone Number"), max_digits=11, decimal_places=0)
    Joinnig_date = models.DateField(("Joining Date"), max_length=50)
    username = models.CharField(max_length=30)
    def __str__(self):

        return self.username  

class Assets(models.Model):
    asset_id = models.IntegerField(primary_key=True)
    asset_name = models.CharField(max_length=30)
    asset_type = models.CharField(max_length=30)
    asset_price = models.IntegerField()
    asset_purchase_date = models.DateField()
    asset_warranty = models.IntegerField()
    asset_status = models.CharField(max_length=30)
    asset_location = models.CharField(max_length=30)
    asset_description = models.CharField(max_length=30)
    def __str__(self):
        return self.asset_name


class AssetAssign(models.Model):
    asset_id = models.ForeignKey(Assets, on_delete=models.CASCADE)
    emp_id = models.ForeignKey(Employess, on_delete=models.CASCADE)
    asset_assign_date = models.DateField()
    asset_return_date = models.DateField()
    asset_assign_status = models.CharField(max_length=30)
    asset_log = models.CharField(max_length=30)
    def __str__(self):
        return self.asset_assign_status