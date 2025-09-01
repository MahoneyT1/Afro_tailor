from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the User model.
    This allows for better management of user accounts in the Django admin panel.
    """
    list_display = ('username', 'email', 'is_seller', 'phone', 'address',
                     'first_name', 'last_name', 'is_active', 'is_staff')

    search_fields = ('username', 'email')
    list_filter = ('is_seller',)
    ordering = ('username',)
