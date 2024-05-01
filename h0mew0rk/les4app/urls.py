from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_les4, name='index_les4'),
    path('product/add/', views.product_form, name='product_form'),
    path('product/<int:product_id>/', views.product_view, name='product_view'),
]