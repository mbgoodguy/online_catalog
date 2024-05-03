from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from employees.models import Employee


# def show_tree(request):
#     employees = Employee.objects.all()
#     current_page = Paginator(list(employees), 20)
#     page = request.GET.get('page')  # Получаем параметр 'page' из GET-запроса
#
#     context = {}
#
#     try:
#         context['employees'] = current_page.page(page)
#     except PageNotAnInteger:
#         # Если параметр 'page' не является целым числом, показываем первую страницу
#         context['employees'] = current_page.page(1)
#     except EmptyPage:
#         # Если номер страницы выходит за пределы допустимых значений, показываем последнюю страницу
#         context['employees'] = current_page.page(current_page.num_pages)
#
#     return render(request, 'tree.html', context)


def show_employees_table(request):
    employees = Employee.objects.all()
    current_page = Paginator(list(employees), 20)
    page = request.GET.get('page')  # Получаем параметр 'page' из GET-запроса

    context = {}

    try:
        context['employees'] = current_page.page(page)
    except PageNotAnInteger:
        # Если параметр 'page' не является целым числом, показываем первую страницу
        context['employees'] = current_page.page(1)
    except EmptyPage:
        # Если номер страницы выходит за пределы допустимых значений, показываем последнюю страницу
        context['employees'] = current_page.page(current_page.num_pages)

    return render(request, 'employees_table.html', context)
