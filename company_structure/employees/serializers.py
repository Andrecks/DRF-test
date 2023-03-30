from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    num_employees = serializers.SerializerMethodField()
    summary_wage = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'num_employees', 'summary_wage']

    def get_num_employees(self, obj):
        return obj.employees.count()

    def get_summary_wage(self, obj):
        return sum([emp.salary for emp in obj.employees.all()])