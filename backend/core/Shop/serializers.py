"""
Serializer for the Shop model.
"""

from rest_framework import serializers
from Shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    """
    Serializer for the Shop model.
    """

    class Meta:
        model = Shop
        fields = ('id', 'name', 'location', 'created_at', 'updated_at', 'owner')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        """uses the request user as the owner 
            of the shop at the point of creation
        """
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)