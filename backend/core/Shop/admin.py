"""
    admin interface for shop model
"""

from django.contrib import admin
from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Shop model.
    This allows for better management of shop instances in the Django admin panel.
    """
    list_display = ('id', 'name', 'location', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'location', 'owner__username', 'owner__email')
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)

    def create(self, request, *args, **kwargs):
        """
        Override the create method to set default values or perform
        additional actions when a new shop is created via the admin interface.
        """
        user = request.user
        return super().create(request, owner=user, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Override the update method to handle any custom logic when
        updating a shop via the admin interface.
        """
        return super().update(request, *args, **kwargs)