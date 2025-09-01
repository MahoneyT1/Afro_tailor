from django.db import models
from django.contrib.auth.models import User



class Cart(models.Model):
    """
    Model representing an item in a user's shopping cart.
    This model links a product to a user and tracks the quantity of the product in the cart.
    """

    user = models.ForeignKey('User.User', on_delete=models.CASCADE, 
                             related_name='cart_items')


    def __str__(self):
        return f"{self.user.username} - {self.user.product.name} (x{self.quantity})"

