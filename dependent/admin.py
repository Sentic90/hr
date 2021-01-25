from django.contrib import admin
from dependent.models import Dependent

@admin.register(Dependent)
class DependentAdmin(admin.ModelAdmin):
    pass
    # list_display = ()
    # list_filter = ()
    # list_editable = ()
    # ordering = ()
    # search_fields = ()
    # fieldsets = ()
    # actions = ()
