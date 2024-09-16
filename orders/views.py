from rest_framework import generics
from orders.models import Order
from orders.serializers import OrderSerializer



class OrdersCreateListView(generics.ListCreateAPIView): 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdersRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
