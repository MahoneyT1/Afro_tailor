from django.db import models


class ProductVariant(models.Model):
    """
    Model representing a variant of a product.
    This can include different sizes, colors, or other attributes.
    """

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Black', 'Black'),
        ('White', 'White'),
    ]

    product = models.ForeignKey('Product.Product', on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='product_variants/', blank=True, null=True)
    in_stock = models.PositiveIntegerField(default=0)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.product.name} - {self.name}"
