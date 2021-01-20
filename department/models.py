from django.db import models


class Department(models.Model):
    class Meta:
        # db_table = 'Department'
        verbose_name_plural = 'Department'

    Dname  = models.CharField(max_length=250)
    Mgr_ssn  = models.ForeignKey('employee.Employee', on_delete=models.CASCADE,blank=True,null=True)
    Mgr_start_date = models.DateTimeField()
    dnumber  = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Dname
        





    