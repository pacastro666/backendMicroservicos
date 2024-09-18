from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product_id', 'product_title', 'product_price', 'quantity', 'total_price']
        read_only_fields = ['id', 'total_price']  # 'total_price' será calculado automaticamente no modelo
