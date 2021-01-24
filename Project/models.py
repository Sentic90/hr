from django.db import models    

class PROJECT(models.Model):
    Pname = models.CharField(max_length=10)
    Pnumber = models.AutoField(primary_key=True)
    Plocation = models.CharField(max_length=10)
    Dnum = models.ForeignKey("Department.DEPARTMENT", on_delete=models.CASCADE, blank=True, null=True)
