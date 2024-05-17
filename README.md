# Инструкция по запуску
- Склонировать репозиторий
- В корне проекта, из терминала выполнить команды:
  - `python manage.py makemigrations`
  - `python manage.py migrate`

- В админке необходимо создать первого юзера, чтобы скрипт наполнения БД сработал
- В `employees/views.py` раскомменитровать методы `save` и `get_random_employee_excluding_self`


- Наполнить данными БД командой `python manage.py seeddb`. В директории `employees/management/commands/seeddb.py`
можно настроить количество генерируемых записей
