from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_temp, name='index_temp'),
    path('client/<int:client_id>/', views.client_products, name='client_products'),
]