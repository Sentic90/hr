from django.db import models

class DEPT_LOCATIONS(models.Model):
    Dnumber = models.ForeignKey("Department.DEPARTMENT", on_delete=models.CASCADE, blank=True, null=True)
    Dlocation = models.CharField(max_length=100)
