from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from les2app.models import Client

class Command(BaseCommand):
    help = "Delete client by id."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Client id')

    def handle(self, *args: Any, **options: Any) -> None:
        pk = options['pk']
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')
        if client is not None:
            client.delete()
        