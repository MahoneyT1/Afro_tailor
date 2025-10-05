"""
    This file includes User and it's scopes
    Client: User(client), tenant: User(designer)
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from Shop.models import Shop


class User(AbstractUser):
    """
    Custom User model that extends the default Django user model.
    This can be used to add additional fields or methods in the future.
    """

    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_designer = models.BooleanField(default=False, blank=True, null=True)
    is_client = models.BooleanField(default=True, blank=True, null=True)
    shop = models.ForeignKey('Shop.Shop', 
                             on_delete=models.SET_NULL, 
                             blank=True, null=True, related_name='users'
                             )

    def __str__(self):
        return f'[{self.id}] ({self.full_name}) ({self.username})'


    


