from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(default='',max_length=15, blank=True)
    address = models.TextField(default='', blank=True)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'
    

class Product(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=100.00, max_digits=8, decimal_places=2)
    count = models.IntegerField(default=1)
    date_add = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default=None, upload_to='products/', blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
    

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Заказ на сумму: {self.total}'
