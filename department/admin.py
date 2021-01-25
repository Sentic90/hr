from django.contrib import admin
from department.models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dnumber', 'dname', 'mgr_ssn')
    # list_filter = ()
    # list_editable = ()
    ordering = ('dnumber', 'dname')
    search_fields = ('dname',)
    # fieldsets = ()
    # actions = ()

# admin.site.register(Department)
