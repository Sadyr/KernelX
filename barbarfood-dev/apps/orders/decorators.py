import functools

from apps.orders.exceptions import UserSessionNotFound
from apps.orders.permissions import get_user_session


def add_session(raise_exception=False):
    def actual_decorator(view_func):

        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):

            session = get_user_session(request.request._request.session_uuid)

            if not session and raise_exception:
                raise UserSessionNotFound

            setattr(request.request._request, 'session', session)
            return view_func(request, *args, **kwargs)
        return wrapper

    return actual_decorator