from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_les6, name='index_les6'),
]