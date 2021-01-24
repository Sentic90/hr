from django.db import models

class WORKS_ON(models.Model):
    Essn = models.ForeignKey("Employee.EMPLOYEE", on_delete=models.CASCADE, blank=True, null=True)
    Pno = models.ForeignKey("Project.PROJECT", on_delete=models.CASCADE, blank=True, null=True)
    Hours = models.TimeField()
