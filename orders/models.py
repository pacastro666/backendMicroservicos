from django.db import models

class Order(models.Model):
    product_id = models.IntegerField()
    product_title = models.CharField(max_length=255)
    product_price = models.FloatField()

    def __str__(self):
        return f"Order {self.id} - {self.product_title}"
