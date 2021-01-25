from django.contrib import admin
from employee.models import Employee

# class EmployeeInline(admin.TabularInline):
#     model = Employee
#     extra = 0
#     ordering = ('fname',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'fname', 'lname', 'gender', 'salary', 'dno')
    list_filter = ('gender', 'dno')
    ordering = ('fname',)
    search_fields = ('fname', 'minit', 'lname', 'address')
    readonly_fields = ('ssn', 'super_ssn', 'dno')
    list_editable = ('fname', 'lname')
    # actions = ()
    fieldsets = (
        (
            'employee info',
            {
                'fields': ('ssn', 'fname', 'minit', 'lname', 'bdate', 'address', 'gender', 'salary', 'super_ssn', 'dno')
            }
        ),
    )
    # inlines = [EmployeeInline]

# admin.site.register(Employee)
