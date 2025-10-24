"""User serializer class
"""
from rest_framework import serializers
from .models import User
from Shop.models import Shop


class UserSerializer(serializers.ModelSerializer):

    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                   'is_designer', 'phone', 'address', 'is_active', 
                   'is_staff', 'products', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'is_designer': {'read_only': False},
            'is_client': {'read_only': True},
            'shop': {'read_only': True},
        }

        read_only_fields = ('id', 'is_active', 'is_staff')

    def create(self, validated_data):
        """
        Create a new user instance, setting the password properly by hashing.
        """
        password = validated_data.pop('password', None)

        if not password:
            raise(serializers.ValidationError("password are required"))

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            del validated_data['password']

        if 'is_designer' in validated_data:
            raise serializers.validationError("You cannot change 'is_designer' field.")

        return super().update(instance, validated_data)
