# В файле seed_db.py
import datetime
import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from employees.models import Employee


class Command(BaseCommand):
    help = 'Заполнение базы данных сотрудниками'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        seeder.add_entity(Employee, 10, {
            'full_name': lambda x: seeder.faker.name(),
            'position': lambda x: random.choice([pos for pos in Employee.Position.choices])[1],
            'date_of_employment': lambda x: seeder.faker.date_between(
                start_date=datetime.date(2021, 1, 1),
                end_date=datetime.date(2024, 1, 1)
            ),
            'salary_in_dollars': lambda x: random.randint(500, 3000)
        })

        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded database with {inserted_pks} employees.'))