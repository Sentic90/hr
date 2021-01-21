from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Employee
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Employee)
class EmployeeAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['Fname', 'Minit', 'Lname', 'ssn', 'Bdate', 'Address', 'Sex', 'Salary', 'Super_ssn', 'dno']
    search_fields = ["ssn", "Address"]
    list_filter =  ["Bdate", "Minit", "Sex", "Salary"]
    search_fields = ['ssn', 'Salary']
    # readonly_fields = 
    # ordering = 
    list_editable = ['ssn']
    # fields
    # fieldsets = 
    # fieldsets_add
    # import & export

# admin.site.register(Employee, EmployeeAdmin)

''' Unregistered Models '''

# admin.site.unregister(User)
# admin.site.unregister(Group)
