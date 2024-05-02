import logging
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, ImageForm
from .models import Product

logger = logging.getLogger(__name__)

def index_les4(request):
    context = dict()
    return render(request,'les4app/index.html',context)


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form1 = ImageForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            logger.info(f'Получили name={name}, description={description}, price={price}, count={count}.')
            product = Product(name=name, description=description, price=price,count=count)
            product.save()
            message = 'Товар сохранён без фото'
            if form1.is_valid():
                image = form1.cleaned_data['image']
                logger.info(f'Получили image={image}.')
                product.image = image
                product.save()
                message = 'Товар сохранён c фото'
    else:
        form = ProductForm()
        form1 = ImageForm()
        message = 'Заполните форму'
    return render(request, 'les4app/product_form.html', {'form': form, 'form1': form1, 'message': message})

def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'prod': product}
    return render(request, 'les4app/product.html', context)