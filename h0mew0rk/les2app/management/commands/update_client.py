from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from les2app.models import Client

class Command(BaseCommand):
    help = "Update client name by id."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='Client id')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args: Any, **options: Any) -> None:
        pk = options.get('pk')
        name = options.get('name')
        client = Client.objects.filter(pk=pk).first()
        client.name= name
        self.stdout.write(f'{client}')
        