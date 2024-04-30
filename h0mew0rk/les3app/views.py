from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Client, Product, Order

# Create your views here.

def index_temp(request):
    context = dict()
    return render(request,'les3app/index.html',context)


def client_products(request,client_id):
    client = get_object_or_404(Client, pk=client_id)
    last_days = [0, 0, 0, 0]
    last_days[0] = timezone.now()
    last_days[1] = timezone.now() - timezone.timedelta(days=7)
    last_days[2] = timezone.now() - timezone.timedelta(days=30)
    last_days[3] = timezone.now() - timezone.timedelta(days=365)
    products = [0,0,0]
    for i in range(3):
        orders = Order.objects.filter(client=client) & Order.objects.filter(date_order__lt=last_days[i]) & Order.objects.filter(date_order__gte=last_days[i + 1])
        products[i] = []
        if orders is not None:
            for order in  orders:
                products[i] += Order.objects.get(pk=order.id).product.all()


    context = {"client" : client.name, 
               'products_week':products[0],
               'products_month':products[1],
               'products_year':products[2],
               }

    return render(request, 'les3app/client_products.html', context)