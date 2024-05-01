from django.db import models
from django.utils import timezone


class Employee(models.Model):
    class Position(models.TextChoices):
        SOFTWARE_DEVELOPER = 'SD', 'Разработчик ПО (Software Developer)'
        SOFTWARE_TEST_ENGINEER = 'STE', 'Инженер по тестированию программного обеспечения (Software Test Engineer)'
        SOFTWARE_ARCHITECT = 'SA', 'Архитектор программного обеспечения (Software Architect)'
        TECHNICAL_WRITER = 'TW', 'Технический писатель (Technical Writer)'
        PRODUCT_MANAGER = 'PM', 'Продуктовый менеджер (Product Manager)'
        PROJECT_MANAGER = 'PJM', 'Менеджер проекта (Project Manager)'
        BUSINESS_ANALYST = 'BA', 'Аналитик бизнес-требований (Business Analyst)'
        UX_UI_DESIGNER = 'UXUI', 'UX/UI дизайнер (UX/UI Designer)'
        DEVOPS_ENGINEER = 'DEVOPS', 'DevOps инженер (DevOps Engineer)'
        SYSTEM_ADMINISTRATOR = 'SYSADM', 'Системный администратор (System Administrator)'
        SOFTWARE_SUPPORT_ENGINEER = 'SSE', 'Инженер сопровождения ПО (Software Support Engineer)'
        DATA_ANALYST = 'DA', 'Аналитик данных (Data Analyst)'
        INFOSEC_ENGINEER = 'INFOSEC', 'Инженер информационной безопасности (Information Security Engineer)'
        TEST_AUTOMATION_ENGINEER = 'TAE', 'Специалист по автоматизации тестирования (Test Automation Engineer)'
        DEPLOYMENT_ENGINEER = 'DE', 'Инженер по развертыванию (Deployment Engineer)'

    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=7, choices=Position.choices)
    date_of_employment = models.DateField(auto_now_add=True)
    supervisor = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
    salary_in_dollars = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name
