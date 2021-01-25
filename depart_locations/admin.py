from django.contrib import admin
from depart_locations.models import Depart_Location

@admin.register(Depart_Location)
class DepartLocationAdmin(admin.ModelAdmin):
    pass
    # list_display = ()
    # list_filter = ()
    # list_editable = ()
    # ordering = ()
    # search_fields = ()
    # fieldsets = ()
    # actions = ()
