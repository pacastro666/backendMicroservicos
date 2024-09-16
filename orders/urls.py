
from django.urls import path
from . import views

urlpatterns = [
    path('comprar/', views.OrdersCreateListView.as_view(), name='create_order'),
    path('comprar/<int:pk>/', views.OrdersRetriveUpdateDestroyView.as_view(), name='create_order'),
]
