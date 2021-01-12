from django.db import models
from django.utils import timezone


class Department(models.Model):
    dnumber = models.AutoField(auto_created=True, primary_key=True)
    dname = models.CharField(max_length=250)
    mgr_ssn = models.ForeignKey("employee.Employee", on_delete=models.SET_NULL, null=True, blank=True)
    mgr_start_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Department'
    
    def __str__(self):
        return self.dname
