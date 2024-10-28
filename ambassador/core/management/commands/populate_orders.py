from typing import Any
from django.core.management import BaseCommand

from django.core.management.base import CommandParser
from faker import Faker

from core.models import Order, OrderItem, User

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:

        parser.add_argument('--user', type=int, default=1, help='ID for the user')
        parser.add_argument('--count', type=int, default=10, help='Number of orders')


    def handle(self, *args: Any, **options: Any) -> str | None:
        user_id = options['user']
        count = options['count']
        faker = Faker()

        user = User.objects.get(pk=user_id)
    
        if not user:
            raise User.DoesNotExist('User not found')
        
        self.stdout.write(f"Creating {count} orders for {user.email}")

        for _ in range(count):
            order = Order.objects.create(
                    transaction_id = faker.iana_id(),
                    user = user,
                    code = faker.ripe_id(),
                    ambassador_email = user.email,
                    first_name = faker.first_name(),
                    last_name = faker.last_name(),
                    email = faker.email(),
                    address = faker.address(),
                    city = faker.city(),
                    country = faker.country(),
                    zip = faker.zipcode(),
                    complete = faker.random_element([True, False]),
            )

            # Create order items for the order
            for _ in range(faker.random_int(min=1, max=10)):
                price = faker.random_int(min=10000, max=500000)
                quantity = faker.random_int(min=1, max=20)

                OrderItem.objects.create(
                    order = order,
                    product_tile = faker.text(max_nb_chars=30),
                    price = price,
                    quantity = quantity,
                    admin_revenue = .9 * price * quantity,
                    ambassador_revenue = .1 * price * quantity
                )