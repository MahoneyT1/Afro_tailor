from django.db import models


class Product(models.Model):
    """
    Model representing a product in the system.
    This model can be extended with additional fields as needed.
    """

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    base_price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='products')

    
    def __str__(self):
        return self.name