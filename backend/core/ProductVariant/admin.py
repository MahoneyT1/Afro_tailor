from django.contrib import admin
from .models import ProductVariant


class ProductVariantAdmin(admin.ModelAdmin):
    """
    Admin interface for ProductVariant model.
    """

    list_display = ('product', 'size', 'color', 'image')
    search_fields = ('product__name', 'name')
    list_filter = ('product',)

admin.site.register(ProductVariant, ProductVariantAdmin)
