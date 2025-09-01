"""
Custom permission class that will control the creation of products
"""
from rest_framework.permissions import BasePermission


class IsSeller(BasePermission):
    """
    Custom permission to only allow sellers to create products.
    """

    def has_permission(self, request, view):
        # Allow POST requests only if the user 
        # is authenticated and is a seller

        return request.method == 'POST' and \
            request.user.is_authenticated and \
            hasattr(request.user, 'is_seller') and \
            request.user.is_seller
