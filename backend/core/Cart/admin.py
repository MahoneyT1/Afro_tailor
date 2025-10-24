from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    """
    Admin interface for Cart model.
    """

    list_display = ['user']
    search_fields = ('user__username',)
    list_filter = ('created_at', 'updated_at')

admin.site.register(Cart, CartAdmin)