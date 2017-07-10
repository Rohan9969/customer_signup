from rest_framework import serializers
from . import models

class CustomerProfileSerializer(serializers.ModelSerializer):
    """A serializer for our customer profile objects."""

    class Meta:
        model = models.Customer
        fields = ('id','email','first_name','last_name','password')
        extra_kwargs = {'passsword': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.Customer(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
