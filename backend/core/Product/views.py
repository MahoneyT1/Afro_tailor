"""View for creating Product
"""
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
from .permissions import IsSeller


class ProductCreateView(generics.CreateAPIView):
    """
    View for creating a new product.
    This view allows authenticated sellers to create new products.
    It uses the ProductSerializer to validate and save the product data.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]


class ProductListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, or deleting a product.
    This view allows authenticated users to perform these actions on products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]

    def get_queryset(self):
        # Optionally filter products by the seller if needed
        return self.queryset.filter(seller=self.request.user)
