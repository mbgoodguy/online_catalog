from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('full_name', 'position', 'date_of_employment', 'supervisor', 'salary_in_dollars', )
    readonly_fields = ['date_of_employment']
