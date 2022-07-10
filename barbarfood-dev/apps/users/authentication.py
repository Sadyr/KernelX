import jwt
from django.conf import settings
from rest_framework_simplejwt.authentication import (
    JWTAuthentication as BaseJWTAuthentication,
)


class JWTAuthentication(BaseJWTAuthentication):

    def get_user(self, validated_token):
        user = super().get_user(validated_token)
        return user
