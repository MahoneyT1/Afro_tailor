"""View for creating Product
"""
from rest_framework.views import APIView
from .models import Product
from .serializer import ProductSerializer
from .permissions import IsSeller
from rest_framework.response import Response
from rest_framework import status


class ProductCreateView(APIView):
    """
    View for creating a new product.
    This view allows authenticated sellers to create new products.
    It uses the ProductSerializer to validate and save the product data.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]

    def create(self, request, *args, **kwargs):
        """ Creates a product"""

        user = self.context['request.user']

        if user.isSeller:
            request.data['seller'] = user.id
            return super().create(request, *args, **kwargs)


class ProductListUpdateDeleteView(APIView):
    """
    View for retrieving, updating, or deleting a product.
    This view allows authenticated users to perform these actions on products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]

    def get_queryset(self):
        # Optionally filter products by the seller if needed
        return self.queryset.filter(seller=self.request.user
        )
    
    def get(self, request, *args, **kwargs):
        """ Lists all products"""
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        """ Updates a product"""
        try:
            product = self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        """ Deletes a product"""
        try:
            product = self.get_queryset().get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"detail": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
