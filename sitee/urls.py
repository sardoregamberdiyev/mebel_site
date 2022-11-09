from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('catalog', catalog, name='catalog'),
    path('contacts', contacts, name='contacts'),
    path('product', product, name='product'),
]
