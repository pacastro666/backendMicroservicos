from rest_framework import generics
from orders.models import Order
from orders.serializers import OrderSerializer



class OrdersCreateListView(generics.ListCreateAPIView): 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def create(self, request, *args, **kwargs):
    #     # Exibe os dados da requisição recebidos na API
    #     print(f"Dados recebidos para criar pedido: {request.data}")
        
    #     # Você pode adicionar validações ou qualquer outra lógica aqui
    #     return super().create(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     # Exibe os dados da requisição, se necessário
    #     print(f"Listando pedidos para o usuário: {request.user}")
    #     return super().list(request, *args, **kwargs)


class OrdersRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
