from rest_framework import serializers
from .models import User
from Cart.models import Cart
from CartItem.serializer import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.
    This serializer handles the conversion of Cart model instances to JSON format
    and vice versa.
    """

    class Meta:
        model = Cart
        fields = ['id', 'user', 'quantity']
        read_only_fields = ['id', 'user']

    # create / overide the create method to handle the creation of a cart
    def create(self, validated_data):
        """overidding create method to accomodate creation of cartItem
        """
        try:
            cart, created = Cart.objects.get_or_create(user=self.context['request'].user)
            if created:
                cart.save()
            
            return super().self.create(user=cart.user, **validated_data)
        except Exception as e:
            raise serializers.ValidationError(
                f"Error creating cart: {str(e)}")
