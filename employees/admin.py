from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('full_name', 'position', 'date_of_employment', 'supervisor', 'salary_in_dollars', )
    readonly_fields = ('date_of_employment', )
    raw_id_fields = ('supervisor', )  #
    search_fields = ('full_name', )  # параметр для поиска в окне выбора руководителя
    list_filter = ('position', 'supervisor', )
    list_per_page = 10

