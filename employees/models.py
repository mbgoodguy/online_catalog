from django.core.exceptions import ValidationError
from django.db import models
from mptt.models import MPTTModel


class Employee(MPTTModel):
    class Position(models.TextChoices):
        SOFTWARE_DEVELOPER = 'SD', 'Software Developer'
        SOFTWARE_TEST_ENGINEER = 'STE', 'Software Test Engineer'
        SOFTWARE_ARCHITECT = 'SA', 'Software Architect'
        TECHNICAL_WRITER = 'TW', 'Technical Writer'
        PRODUCT_MANAGER = 'PM', 'Product Manager'
        PROJECT_MANAGER = 'PJM', 'Project Manager'
        BUSINESS_ANALYST = 'BA', 'Business Analyst'
        UX_UI_DESIGNER = 'UXUI', 'UX/UI Designer'
        DEVOPS_ENGINEER = 'DEVOPS', 'DevOps Engineer'
        SYSTEM_ADMINISTRATOR = 'SYSADM', 'System Administrator'
        SOFTWARE_SUPPORT_ENGINEER = 'SSE', 'Software Support Engineer'
        DATA_ANALYST = 'DA', 'Data Analyst'
        INFOSEC_ENGINEER = 'INFOSEC', 'Information Security Engineer'
        TEST_AUTOMATION_ENGINEER = 'TAE', 'Test Automation Engineer'
        DEPLOYMENT_ENGINEER = 'DE', 'Deployment Engineer'

    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=Position.choices)
    date_of_employment = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinates')
    salary_in_dollars = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.full_name}: {self.position}'

    def clean(self):
        if self.parent == self:
            raise ValidationError("Сотрудник не может быть своим собственным руководителем.")

    class MPTTMeta:
        order_insertion_by = ['full_name']

    # Расскомментировать после добавления первого сотрудника в админке.
    # def save(self, *args, **kwargs):
    #     if self.supervisor is None:
    #         # Если руководитель пустой, назначаем случайного сотрудника
    #         self.supervisor = self.get_random_employee_excluding_self()
    #     super().save(*args, **kwargs)
    #
    # def get_random_employee_excluding_self(self):
    #     # Получить случайного сотрудника, исключая текущего
    #     all_employees_count = Employee.objects.exclude(id=self.id).count()
    #     random_index = randint(0, all_employees_count - 1)
    #     random_employee = Employee.objects.exclude(id=self.id)[random_index]
    #     return random_employee
