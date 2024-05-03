from django.contrib import admin
from .models import Client, Product,Order
from decimal import Decimal

@admin.action(description="Обнулить количество товара")
def set_zero(modeladmin, request, queryset):
    queryset.update(count=0)


@admin.action(description="Уменьшить на 10 процентов цену товара")
def reducing_price(modeladmin, request, queryset):
    for prod in queryset.all():
        prod.price *= Decimal("0.9")
        prod.save()


@admin.action(description="Увеличить на 10 процентов цену товара")
def increase_price(modeladmin, request, queryset):
    for prod in queryset.all():
        prod.price *= Decimal("1.1")
        prod.save()


@admin.action(description="Удалить телефон клиента")
def del_phone(modeladmin, request, queryset):
    queryset.update(phone='')

class ProductAdmin(admin.ModelAdmin):
    """Список товаров"""
    list_display = ('name', 'price', 'count')
    ordering = ('name', '-count')
    list_filter = ('date_add',)
    search_fields = ('name',)
    search_help_text = 'Поиск по полю название товара (name)'
    actions = (set_zero, reducing_price, increase_price)
    """Отдельный товар"""
    fields = ('name', 'price', 'count', 'description', 'date_add', 'image')
    readonly_fields = ('date_add', 'image')


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ('name', 'email', 'phone')
    ordering = ('name',)
    list_filter = ('date_reg',)
    search_fields = ('name', 'email')
    search_help_text = 'Поиск имени и e-mail клиента (name, email)'
    actions = (del_phone,)
    """Отдельный клиент"""
    fields = ('name', 'email', 'phone', 'date_reg', 'address')
    readonly_fields = ('date_reg',)

class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ('client', 'total', 'date_order')
    ordering = ('-total',)
    list_filter = ('date_order',)
    """Отдельный заказ"""
    readonly_fields = ('date_order',)
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Товары',
            {
                'classes': ['collapse'],
                'description': 'Товары, входящие в заказ',
                'fields': ['product'],
            },
        ),
        (
            'Общая сумма заказа',
            {
                'fields': ['total'],
            }
        ),
        (
        'Дата оформления заказа',
            {
                'fields': ['date_order'],
            }
        ),
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)