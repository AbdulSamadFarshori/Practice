from rest_framework import serializers
from website.models import Employee



class EmployeeSerializer(serializers.ModelSerializer):

    age = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'DOB', 'age', 'is_working', 'created_at', 'updated_at', 'department_name']

    def get_age(self, obj):

        cur_month = 5
        cur_year = 2023
        employee_month = obj.DOB.month
        employee_year = obj.DOB.year
        age = cur_year - employee_year

        if cur_month < employee_month:
            age -= 1
        return age

        


    