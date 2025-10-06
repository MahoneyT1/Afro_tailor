"""
    shop api views
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShopSerializer
from .models import Shop


class ShopCreateView(APIView):
    """
    View to create a new shop.
    """

    def post(self, request, *args, **kwargs):
        serializer = ShopSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            shop = serializer.save()
            return Response(ShopSerializer(shop).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShopRetrieveUpdateDeleteView(APIView):
    """
    View to retrieve, update or delete a shop.
    """

    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        shop = self.get_object(pk)
        if shop is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        shop = self.get_object(pk)
        if shop is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShopSerializer(shop, data=request.data, context={'request': request})
        if serializer.is_valid():
            shop = serializer.save()
            return Response(ShopSerializer(shop).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        shop = Shop.objects.filter(pk=pk).first()
        if shop is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
