from rest_framework import permissions
from uuid import UUID
from apps.orders.exceptions import UserSessionNotFound
from apps.users.models import UserSession


def is_valid_uuid(value, version=4):
    try:
        UUID(value, version=version)
        return True
    except ValueError:
        return False


def get_user_session(uuid):
    if is_valid_uuid(uuid):
        return UserSession.objects.filter(uuid=uuid).select_related(
            'cart', 'address'
        ).first()


class UserSessionPropertyPermission(permissions.BasePermission):
    """
    Validate and add workflow property
    """

    def has_permission(self, request, view):
        session = get_user_session(request.session_uuid)
        if not session:
            raise UserSessionNotFound

        setattr(request, 'session', session)
        return True