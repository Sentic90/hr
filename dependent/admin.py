from django.contrib import admin
from dependent.models import Dependent

@admin.register(Dependent)
class DependentAdmin(admin.ModelAdmin):
    list_display = ('Essn', 'Dependent_name', 'Relationship')
    list_filter = ('Essn', 'gender')
    # list_editable = ('Dependent_name', 'Relationship')
    ordering = ('Essn', 'Dependent_name', 'bdate')
    search_fields = ('Dependent_name',)
    # fieldsets = ()
    # actions = ()
