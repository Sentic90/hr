from django.contrib import admin
from project.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pnumber', 'pname', 'plocation', 'dnumber')
    list_filter = ('dnumber',)
    list_editable = ('pname', 'plocation')
    ordering = ('pnumber', 'pname')
    search_fields = ('pname', 'plocation')
    # fieldsets = ()
    # actions = ()
