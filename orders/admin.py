from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'product_title', 'product_price')
    search_fields = ('product_title',)
