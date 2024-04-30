from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Имя:{self.name}, e-mail:{self.email}, Телефон={self.phone}, Адрес:{self.address}, Дата регистрации:{self.date_reg}'
    

class Product(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Название:{self.name}, Описание:{self.description}, Цена:{self.price}, Количество:{self.count}, Дата добавления:{self.date_add}'
    

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Общая сумма заказа:{self.total}, дата оформления заказа:{self.date_order}'
