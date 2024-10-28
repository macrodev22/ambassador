from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from faker import Faker

from core.models import User

class Command(BaseCommand):
    
    help = 'Create dummy ambassadors'

    def add_arguments(self, parser: CommandParser) -> None:
        #Optional arg
        parser.add_argument('--count', type=int, default=30, help='Indicates the number of ambassadors to be created')

    def handle(self, *args: Any, **options: Any) -> str | None:
        count = options['count']
        self.stdout.write(f"Adding {count} ambassadors to DB...")

        faker = Faker()
        for _ in range(count):
            user = User.objects.create(
                first_name = faker.first_name(),
                last_name = faker.last_name(),
                email = faker.email(),
                password='',
                is_ambassador = True,
            )

            user.set_password('testpassword')
            user.save()


