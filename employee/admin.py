from django.contrib import admin
from .models import Employee, Department, Managers
# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Managers)