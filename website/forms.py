from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    name = forms.CharField(max_length=255, initial='Employee')

    class Meta:
        model = Employee
        fields = "__all__"