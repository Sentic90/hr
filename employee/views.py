from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Employee


class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employee'