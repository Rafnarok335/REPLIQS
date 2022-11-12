from django.db import models
from django.contrib.auth.models import User
from Company.models import Employee
# Create your models here.


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
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset_assign_date = models.DateField()
    asset_return_date = models.DateField()
    asset_assign_status = models.CharField(max_length=30)
    asset_log = models.CharField(max_length=30)
    def __str__(self):
        return self.asset_assign_status