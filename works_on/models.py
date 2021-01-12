from django.db import models
from employee.models import Employee
from project_employee.models import ProjectEmployee


class WorksOn(models.Model):
    class Meta:
        verbose_name_plural = "Works On"

    hours = models.CharField(max_length=250)
    
    #forignkey 
    Pno  = models.ForeignKey(ProjectEmployee, on_delete=models.CASCADE, null=True, blank=True)
    Essn  = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)