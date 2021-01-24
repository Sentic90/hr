from django.db import models
# Create your models here.

class employee(models.model):

    fname=models.CharField(max_length=50,unique=True)
    minit=models.CharField(max_length=1)
    lname=models.CharField(max_length=50)

    bdate=models.datefield()
    address=models.TextField(max_length=50)
    Male = "M"
    Female = 'F'
    sex_choices = [
        ('M' = "Male"),
    ('F' = "Female"),
                  ]
    sex-choices = models.CharField(
        max_length=1,
        choices=sex_choices,
        default=Male,
    )

    def is_upperclass(employee):
        return employee.sex_choices in {employee.M, employee.F}

    salary=models.IntegerField(max_length=50)
    super_ssn=models.ForeignKey('Ssn', on_delete=models.CASCADE)


class Ssn(models.Model):
    ssn = models.IntigerField(max_length=9)

super_ssn=models.ForeignKey('employee.Ssn', on_delete=models.CASCADE)

dno=models.IntigerField(max_length=1)

