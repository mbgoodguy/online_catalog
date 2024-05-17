# В файле seed_db.py
import datetime
import os
import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from employees.models import Employee


class Command(BaseCommand):
    help = 'Заполнение базы данных сотрудниками'

    def handle(self, *args, **kwargs):
        images_path = 'media/images/2024/05/03'
        image_files = os.listdir('media/images/2024/05/03')

        seeder = Seed.seeder()
        existing_employees = Employee.objects.all()

        if not os.path.exists(images_path):
            self.stdout.write(self.style.ERROR(f'Path {image_files} does not exist.'))
            return

        if not image_files:
            self.stdout.write(self.style.ERROR(f'No images found in {image_files}.'))
            return

        if not image_files:
            self.stdout.write(self.style.ERROR(f'No images found in {image_files}.'))
            return

        seeder.add_entity(Employee, 5, {
            'full_name': lambda x: seeder.faker.name(),
            'position': lambda x: random.choice(Employee.Position.choices)[1],
            'date_of_employment': lambda x: seeder.faker.date_between(
                start_date=datetime.date(2021, 1, 1),
                end_date=datetime.date(2024, 1, 1)
            ),
            'salary_in_dollars': lambda x: random.randint(500, 3000),
            'parent': lambda x: random.choice(existing_employees),
            'level': lambda x: 0,
            'employee_img': lambda x: os.path.join('images/2024/05/03', random.choice(image_files))
        })

        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded database with {inserted_pks} employees.'))
