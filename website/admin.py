from django.contrib import admin
from .models import Employee, Department
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [col.name for col in Employee._meta.get_fields()]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = ['name']

