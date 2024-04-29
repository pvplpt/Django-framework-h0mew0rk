from typing import Any
from django.core.management.base import BaseCommand
from les2app.models import Client

class Command(BaseCommand):
    help = "Ceate client"


    def handle(self, *args: Any, **options: Any) -> None:
        new_client = Client(name=f'Pavel', email=f'pavel@mail.ru',phone=f'+79191123654', address=f'ул.Ленина, д.1, кв.111')
        new_client.save()
        self.stdout.write(f'{new_client}')
        