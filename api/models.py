from django.db import models
from tastypie.resources import ModelResource
from employee.models import Employee

class EmployeeResoursce(ModelResource):
    class Meta:
        queryset = Employee.objects.all()
        resource_name = 'employee'
