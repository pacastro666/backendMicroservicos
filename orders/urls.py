
from django.urls import path
from .views import create_order

urlpatterns = [
    path('comprar/', create_order, name='create_order'),
]
