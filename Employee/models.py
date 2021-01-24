from django.db import models

class EMPLOYEE(models.Model):
    Fname = models.CharField(max_length=10)
    Minit = models.CharField(max_length=10)
    Lname = models.CharField(max_length=10)
    Bdate = models.DateField()
    Address = models.CharField(max_length=100)
    Sex = models.CharField(max_length=10)
    Salary = models.IntegerField()
    Super_ssn = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    Dno = models.ForeignKey("Department.DEPARTMENT", on_delete=models.CASCADE, blank=True, null=True)
    ssn = models.AutoField(primary_key=True)
