from django.contrib import admin
from project.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
    # list_display = ()
    # list_filter = ()
    # list_editable = ()
    # ordering = ()
    # search_fields = ()
    # fieldsets = ()
    # actions = ()
