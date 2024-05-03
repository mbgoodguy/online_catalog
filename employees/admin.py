from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from employees.models import Employee


class EmployeeAdmin(MPTTModelAdmin):
    fields = ('full_name', 'position', 'date_of_employment', 'parent', 'salary_in_dollars', 'employee_img')
    readonly_fields = ('date_of_employment',)
    raw_id_fields = ('parent',)  #
    search_fields = ('full_name',)  # параметр для поиска в окне выбора руководителя
    list_filter = ('position', 'parent',)
    list_per_page = 10


admin.site.register(Employee, EmployeeAdmin)
