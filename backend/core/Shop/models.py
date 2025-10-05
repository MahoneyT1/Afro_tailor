from django.db import models
import uuid


class Shop(models.Model):
    """
    Model representing a shop.
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField('User.User', 
                                 on_delete=models.CASCADE, related_name='shops')

    def __str__(self):
        return f'[{self.name}] owned by {self.owner.username}'
