from django.shortcuts import render

from employees.models import Employee


def show_tree(request):
    employees = Employee.objects.all()

    return render(request, 'tree.html', context={'employees': employees})
