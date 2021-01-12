from django.db import models


class DeptLocations(models.Model):
    class Meta:
        verbose_name_plural = 'Depts Locations'

    dlocation = models.CharField(max_length=250)

    #ForeignKey
    dnumber = models.ForeignKey("department.Department", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.dlocation