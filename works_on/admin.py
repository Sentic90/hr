from django.contrib import admin
from works_on.models import works_on

@admin.register(works_on)
class WorksOnAdmin(admin.ModelAdmin):
    list_display = ('Pno', 'Essn')
    list_filter = ('Pno', 'Essn')
    # list_editable = ()
    ordering = ('Pno',)
    # search_fields = ('')
    # fieldsets = ()
    # actions = ()

# admin.site.register(works_on)
