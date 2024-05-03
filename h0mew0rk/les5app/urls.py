from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_les5, name='index_les5'),
]