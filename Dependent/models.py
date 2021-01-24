from django.db import models

class DEPENDENT(models.Model):

    Essn = models.ForeignKey("Employee.EMPLOYEE", on_delete=models.CASCADE, blank=True, null=True)
    Dependent_name = models.CharField(max_length=10)
    Sex = models.CharField(max_length=5)
    Bdate = models.DateField()
    Relationship = models.CharField(max_length=20)
