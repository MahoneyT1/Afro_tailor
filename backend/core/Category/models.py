"""
Category models for the application.
"""

from django.db import models


class Category(models.Model):
    """
    Model representing a category.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcategories'
    )

    def __str__(self):
        return self.name


