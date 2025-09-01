"""Product serializer
"""
from rest_framework import serializers
from .models import Product
from User.serializer import UserSerializer
from ProductVariant.models import ProductVariant
from ProductVariant.serializer import ProductVariantSerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    This serializer handles the conversion of Product model instances to JSON format
    and vice versa.
    """
    seller = UserSerializer(read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 
                  'base_price', 'image', 'seller', 'stock', 
                  'category', 'created_at', 'updated_at']
        read_only_fields = ['id', 'seller', 'created_at', 'updated_at']

    def create(self, validated_data):
        variants_data = validated_data.pop('variants', [])
        product = Product.objects.create(**validated_data)

        for variant_data in variants_data:
            ProductVariantSerializer.objects.create(product=product, **variant_data)
        return product