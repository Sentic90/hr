from django.contrib import admin
from depart_locations.models import Depart_Location

@admin.register(Depart_Location)
class DepartLocationAdmin(admin.ModelAdmin):
    list_display = ('dnumber', 'dlocation')
    list_filter = ('dlocation',)
    list_editable = ('dlocation',)
    ordering = ('dnumber', 'dlocation')
    search_fields = ('dlocation',)
    # fieldsets = ()
    # actions = ()
