# mi_aplicacion/urls.py
from django.urls import path
from .views import hola_mundo

urlpatterns = [
    path('hola/', hola_mundo, name='hola_mundo'),
]