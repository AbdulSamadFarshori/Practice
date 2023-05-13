from django.db import models
from django.utils import timezone 
# Create your models here.

DEPARTMENT = (('ACCOUNT', 'ACCOUNT'),
              ('FINANCE', 'FINANCE'),
              ('HR', 'HR'),
              ('MARKETING', 'MARKETING'),
              ('OPERATION', 'OPERATION'),
              ('SALES', 'SALES'),
              ('IT', 'IT'))

class Department(models.Model):

    name = models.CharField(max_length=20, choices=DEPARTMENT, null=True, blank=True)

    def __str__(self):
        return self.name



GENDER = (('M', 'Male'), 
          ('F', 'Female'))

class Employee(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    DOB = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER)
    is_working = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


