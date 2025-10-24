from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for Product model.
    """

    list_display = ('name', 'category', 'base_price', 'stock')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
