from django.db import models
from department.models import Department


class Employee(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    ssn = models.AutoField(auto_created=True, primary_key=True)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    minit = models.IntegerField()
    bdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    salary = models.IntegerField()
    super_ssn = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    dno = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Employee'

    def __str__(self):
        return f"{self.fname} {self.lname}"