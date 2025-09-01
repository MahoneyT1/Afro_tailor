from django.db import models


class OrderItem(models.Model):
    """
    Model representing an item in an order.
    This links a product variant to an order and tracks the quantity of the variant ordered.
    """

    order = models.ForeignKey('Order.Order', on_delete=models.CASCADE, related_name='items')
    variant = models.ForeignKey('ProductVariant.ProductVariant', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.order.id} - {self.variant.product.name} (x{self.quantity})"