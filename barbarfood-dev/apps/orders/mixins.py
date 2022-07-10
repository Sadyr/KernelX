from rest_framework.permissions import AllowAny

from apps.common.mixins import JSONRendererMixin
from apps.orders.permissions import UserSessionPropertyPermission


class UsersessionPropertyMixin:

    @property
    def session(self):
        return getattr(self.context.get('request'), 'session')


class PublicSessionAPIMixin:
    permission_classes = [AllowAny, UserSessionPropertyPermission]


class PublicSessionJSONRendererMixin(JSONRendererMixin, PublicSessionAPIMixin):
    ...

