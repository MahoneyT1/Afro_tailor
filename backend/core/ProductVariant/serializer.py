from rest_framework.serializers import ModelSerializer
from Product.models import Product



class ProductVariantSerializer(ModelSerializer):
    """
    Serializer for the Product model.
    This serializer is used to convert Product instances to JSON and validate incoming data.
    """
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True, 'max_length': 255},
            'description': {'required': True, 'max_length': 1000},
            'price': {'required': True, 'min_value': 0},
            'in_stock': {'required': True, 'min_value': 0},
        }

        verbose_name = 'Product Variant'
