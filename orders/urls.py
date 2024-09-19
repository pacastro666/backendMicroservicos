from django.urls import path
from . import views

urlpatterns = [
    # POST 
    path('comprar/', views.OrderCreateView.as_view(), name='create_order'),
    
    # GET 
    path('comprar/list/', views.OrderListView.as_view(), name='list_orders'),
    
    # GET 
    path('comprar/<int:pk>/', views.OrderDetailView.as_view(), name='retrieve_order'),
    
    # PUT 
    path('comprar/<int:pk>/update/', views.OrderUpdateView.as_view(), name='update_order'),
    
    # DELETE 
    path('comprar/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='delete_order'),
]
