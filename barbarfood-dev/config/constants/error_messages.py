from .error_codes import *
from config.settings import Languages
from datetime import date

ERROR_MESSAGES = {
    f"{NO_ACTIVE_ACCOUNT}_{Languages.RUSSIAN}": ("NO_ACTIVE_ACCOUNT_RU_MSG", ""),
    f"{NO_ACTIVE_ACCOUNT}_{Languages.KAZAKH}": ("NO_ACTIVE_ACCOUNT_KK_MSG", ""),
    f"{NO_ACTIVE_ACCOUNT}_{Languages.ENGLISH}": ("NO_ACTIVE_ACCOUNT_EN_MSG", ""),

    f"{NOT_AUTHENTICATED}_{Languages.RUSSIAN}": ("NOT_AUTHENTICATED_RU_MSG", ""),
    f"{NOT_AUTHENTICATED}_{Languages.KAZAKH}": ("NOT_AUTHENTICATED_KK_MSG", ""),
    f"{NOT_AUTHENTICATED}_{Languages.ENGLISH}": ("NOT_AUTHENTICATED_EN_MSG", ""),

    f"{INVALID_INPUT_DATA}_{Languages.RUSSIAN}": ("INVALID_INPUT_DATA_RU_MSG", ""),
    f"{INVALID_INPUT_DATA}_{Languages.KAZAKH}": ("INVALID_INPUT_DATA_KK_MSG", ""),
    f"{INVALID_INPUT_DATA}_{Languages.ENGLISH}": ("INVALID_INPUT_DATA_EN_MSG", ""),

    f"{INVALID_OTP}_{Languages.RUSSIAN}": ("INVALID_OTP_RU_MSG", ""),
    f"{INVALID_OTP}_{Languages.KAZAKH}": ("INVALID_OTP_KK_MSG", ""),
    f"{INVALID_OTP}_{Languages.ENGLISH}": ("INVALID_OTP_EN_MSG", ""),

    f"{USER_ALREADY_EXISTS}_{Languages.RUSSIAN}": ("USER_ALREADY_EXISTS_RU_MSG", ""),
    f"{USER_ALREADY_EXISTS}_{Languages.KAZAKH}": ("USER_ALREADY_EXISTS_KK_MSG", ""),
    f"{USER_ALREADY_EXISTS}_{Languages.ENGLISH}": ("USER_ALREADY_EXISTS_EN_MSG", ""),

    f"{NOT_FOUND}_{Languages.RUSSIAN}": ("NOT_FOUND_RU_MSG", ""),
    f"{NOT_FOUND}_{Languages.KAZAKH}": ("NOT_FOUND_KK_MSG", ""),
    f"{NOT_FOUND}_{Languages.ENGLISH}": ("NOT_FOUND_EN_MSG", ""),

    f"{OTP_RESEND_TIME_LIMIT}_{Languages.RUSSIAN}": ("OTP_RESEND_TIME_LIMIT_RU_MSG", ""),
    f"{OTP_RESEND_TIME_LIMIT}_{Languages.KAZAKH}": ("OTP_RESEND_TIME_LIMIT_KK_MSG", ""),
    f"{OTP_RESEND_TIME_LIMIT}_{Languages.ENGLISH}": ("OTP_RESEND_TIME_LIMIT_EN_MSG", ""),

    f"{USER_NOT_FOUND}_{Languages.RUSSIAN}": ("USER_NOT_FOUND_RU_MSG", ""),
    f"{USER_NOT_FOUND}_{Languages.KAZAKH}": ("USER_NOT_FOUND_KK_MSG", ""),
    f"{USER_NOT_FOUND}_{Languages.ENGLISH}": ("USER_NOT_FOUND_EN_MSG", ""),

    f"{ADDRESS_NOT_FOUND}_{Languages.RUSSIAN}": ("ADDRESS_NOT_FOUND_RU_MSG", ""),
    f"{ADDRESS_NOT_FOUND}_{Languages.KAZAKH}": ("ADDRESS_NOT_FOUND_KK_MSG", ""),
    f"{ADDRESS_NOT_FOUND}_{Languages.ENGLISH}": ("ADDRESS_NOT_FOUND_EN_MSG", ""),
    'DATE_ESTABLISHED': (date(1972, 11, 30), "wqeqw"),
}
