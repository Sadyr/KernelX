from rest_framework.permissions import AllowAny

from .renderers import JSONRenderer


class JSONRendererMixin:
    renderer_classes = [JSONRenderer]


class PublicAPIMixin:
    permission_classes = [AllowAny]


class PublicJSONRendererMixin(JSONRendererMixin, PublicAPIMixin):
    ...


class UserPropertyMixin:

    @property
    def user(self):
        if self.context.get('request').user.is_authenticated:
            return self.context.get('request').user

    @property
    def auth_user(self):
        if self.context.get('request').auth is not None:
            return self.context.get('request').auth

