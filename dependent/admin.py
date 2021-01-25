import csv

from django.contrib import admin
from dependent.models import Dependent
from django.http import HttpResponse

def exportToCSV(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dependent.csv"'
    writer = csv.writer(response)
    writer.writerow(['Essn', 'Dependent Name', 'Gender', 'Relationship', 'Birth Date'])
    books = queryset.values_list('Essn', 'Dependent_name', 'gender', 'Relationship', 'bdate')
    for book in books:
        writer.writerow(book)
    return response

exportToCSV.short_description = 'Export to csv'

@admin.register(Dependent)
class DependentAdmin(admin.ModelAdmin):
    list_display = ('Essn', 'Dependent_name', 'Relationship')
    list_filter = ('Essn', 'gender')
    # list_editable = ('Dependent_name', 'Relationship')
    ordering = ('Essn', 'Dependent_name', 'bdate')
    search_fields = ('Dependent_name',)
    # fieldsets = ()
    actions = (exportToCSV,)
