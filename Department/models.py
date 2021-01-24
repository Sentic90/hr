from django.db import models

class DEPARTMENT(models.Model):
    Dname = models.CharField(max_length=20)
    Mgr_ssn = models.ForeignKey("Employee.EMPLOYEE", on_delete=models.CASCADE )
    Mgr_start_date = models.DateField()
    Dnumber = models.AutoField(primary_key=True)


