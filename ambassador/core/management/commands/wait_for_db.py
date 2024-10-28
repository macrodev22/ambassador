from typing import Any
from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:

        self.stdout.write('Waiting for Database connection...')

        conn = None

        while not conn:

            try:
                conn = connections['default']
            
            except OperationalError:
                self.stdout.write('Database unavailable!🤪...waiting for 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available😁😎'))


        # return super().handle(*args, **options)