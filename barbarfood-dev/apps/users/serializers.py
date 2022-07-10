from rest_framework import serializers

from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "mobile_phone",
            "name",
            "email",
            "is_active"
        ]


class UserViewSerializer(serializers.ModelSerializer):
    """
    List, Retrieve serializer for User model
    """
    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "first_name", "last_name",
            "email",
            "is_active"
        ]
