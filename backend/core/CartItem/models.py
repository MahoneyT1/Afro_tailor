from django.db import models


class CartItem(models.Model):
    """
    Model representing an item in a user's
    shopping cart. This model links a product
    variant to a user and tracks the quantity 
    of the product in the cart.
    """
    cart = models.ForeignKey('Cart.Cart', on_delete=models.CASCADE, related_name='items')
    variant = models.ForeignKey('ProductVariant.ProductVariant', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.variant.name} (x{self.quantity})"