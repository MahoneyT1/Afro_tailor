from django.db import models
from datetime import datetime
from django.utils import timezone
from User.models import User


class Cart(models.Model):
    """
    Model representing an item in a user's shopping cart.
    This model links a product to a user and tracks the quantity of the product in the cart.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             related_name='cart_items')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} - {self.product.name} (x{self.quantity})"

