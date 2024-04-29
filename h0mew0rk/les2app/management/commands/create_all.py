from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from les2app.models import Client, Product, Order

class Command(BaseCommand):
    help = "Ceate All"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('total', type=int, help='Всего записей')

    def handle(self, *args: Any, **options: Any) -> None:
        count = options['total']
        for i in range(1, count + 1):
            new_client = Client(name=f'Клиент{i}', email=f'client{i}@mail.ru',phone=f'+7919{i}123654'[:12], address=f'ул.Ленина, д.1, кв.{i}')
            new_client.save()
            new_product = Product(name=f'Товар{i}', description=f'Описание{i}', price=(i * 100 + i * 10 + i) / 10, count=i)
            new_product.save()
            order = Order(client=new_client, total=new_product.price * new_product.count)
            order.save()
            order.product.add(new_product)
            order.save()
        self.stdout.write(f'Создано {count} записей.')
        