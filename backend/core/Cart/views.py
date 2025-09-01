"""
    cartItems = view
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CartSerializer
from .models import Cart


class CartListCreateView(APIView):
    """
    View to list and create carts.
    """

    def get(self, request):
        """
        List all carts.
        """
        try:
            carts = Cart.objects.all()
            serializer = CartSerializer(carts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"detail": "No carts found."}, 
                            status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        Create a new cart.
        """
        serializer = CartSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            cart = serializer.save()
            return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)