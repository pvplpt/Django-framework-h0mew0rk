from typing import Any
from django.core.management.base import BaseCommand
from les2app.models import Client

class Command(BaseCommand):
    help = "Get all clients."


    def handle(self, *args: Any, **options: Any) -> None:
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')
        