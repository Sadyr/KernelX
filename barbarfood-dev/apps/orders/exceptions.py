from rest_framework.exceptions import APIException
from config.constants.error_codes import ITEM_NOT_FOUND, CAN_NOT_ADD_ZERO_COUNT_ITEM, USER_SESSION_NOT_FOUND


class ItemNotFound(APIException):
    status_code = 400
    default_code = ITEM_NOT_FOUND


class CanNotAddZeroCountItem(APIException):
    status_code = 400
    default_code = CAN_NOT_ADD_ZERO_COUNT_ITEM


class UserSessionNotFound(APIException):
    status_code = 400
    default_code = USER_SESSION_NOT_FOUND