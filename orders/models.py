from django.db import models

class Order(models.Model):
    product_id = models.IntegerField()
    product_title = models.CharField(max_length=255)
    product_price = models.FloatField()
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField()

    def save(self, *args, **kwargs):
        self.total_price = self.product_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - {self.product_title} (Qty: {self.quantity})"
