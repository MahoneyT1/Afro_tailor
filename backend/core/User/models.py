from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model that extends the default Django user model.
    This can be used to add additional fields or methods in the future.
    """

    is_seller = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username
