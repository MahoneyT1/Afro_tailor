from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the User model.
    This allows for better management of user accounts in the Django admin panel.
    """
    list_display = ('id', 'username', 'email', 'phone', 'address', 'is_designer',
                     'first_name', 'last_name', 'is_active', 'is_staff')

    search_fields = ('username', 'email')
    list_filter = ('is_designer',)
    ordering = ('username',)

    def create(self, request, *args, **kwargs):
        """
        Override the create method to set default values or perform
        additional actions when a new user is created via the admin interface.
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Override the update method to handle any custom logic when
        updating a user via the admin interface.
        """
        return super().update(request, *args, **kwargs)
