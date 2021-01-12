from django.db import models


class DependentName(models.Model):
    class Meta:
        verbose_name_plural = 'Dependent Name'
    
    dependent_name  =  models.CharField(max_length=250, primary_key=True, default='dependant')
    sex  =  models.CharField(max_length=250)
    bdate  =  models.DateField(null=True, blank=True)
    relationship =  models.CharField(max_length=250)
    # ForienKey
    essn  =  models.ForeignKey("employee.Employee", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.dependent_name
    