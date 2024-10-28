from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from faker import Faker
from random import randrange

from core.models import Product

class Command(BaseCommand):

    help = 'Create some dummy products'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--count', type=int, default=10, help='Number of products to add')

    def handle(self, *args: Any, **options: Any) -> str | None:
        count = options['count']
        faker = Faker()
        self.stdout.write(f"Creating {count} products")
        
        for _ in range(count):
            product = Product.objects.create(
                title = faker.name(),
                description = faker.text(100),
                image = faker.image_url(),
                price = randrange(10000,250000)
            )

            product.save()