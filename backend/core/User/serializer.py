"""User serializer class
"""
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = 'User.User'
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                   'is_seller', 'phone', 'address', 'is_active', 'is_staff', 'products')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
        }

        read_only_fields = ('id', 'is_active', 'is_staff')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            del validated_data['password']
        return super().update(instance, validated_data)
