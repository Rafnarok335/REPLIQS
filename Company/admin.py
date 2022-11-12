from django.contrib import admin
from Company.models import Employee, Manager , User
# Register your models here.
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(User)