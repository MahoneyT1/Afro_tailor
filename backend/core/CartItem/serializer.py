from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.
    This serializer handles the conversion of CartItem model instances to JSON format
    and vice versa.
    """
    cart = serializers.PrimaryKeyRelatedField(),
    variant = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'price', 'variant']
        read_only_fields = ['id', 'cart', 'price']

    # override the create method to handle the creation of a cart item
    def create(self, validated_data):
        """overriding create method to accommodate creation of cart item"""
        user = self.context['request'].user

        cart = user.cart
        if not cart:
            raise serializers.ValidationError("Cart does not exist for the user.")

        try:
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                variant=validated_data['variant'],
                defaults={'quantity': validated_data.get('quantity', 1)}
            )
            if created:
                cart_item.save()
                return cart_item

            return super().self.create(cart=user.cart, **validated_data)
        except Exception as e:
            raise serializers.ValidationError(
                f"Error creating cart item: {str(e)}")