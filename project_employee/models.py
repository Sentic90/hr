from django.db import models


class ProjectEmployee(models.Model):
    ''' I've changed the project model ==> ProjectEmployee'''

    class Meta:
        verbose_name_plural = 'Project Employee'
    
    pnumber = models.AutoField(auto_created=True, primary_key=True)
    pname  = models.CharField(max_length=250)
    plocation  = models.CharField(max_length=250)
    #ForeignKey
    dnum = models.ForeignKey("department.Department", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.pname
