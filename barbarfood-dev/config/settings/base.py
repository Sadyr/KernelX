import base64
import os
from collections import OrderedDict
from datetime import timedelta
from config.constants.error_messages import ERROR_MESSAGES
from config.constants.contact_information import CONTACT_INFORMATION
from config.settings import Languages

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DOCUMENT_GENERETOR_URL = ""

DEBUG = True
SECRET_KEY = "TEST_TEST"
ALLOWED_HOSTS = ['*']

OTP_LENGTH = 4
OTP_VALIDITY_PERIOD = 1.5

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "phonenumber_field",
    "constance"
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.common.apps.CommonConfig',
    'apps.users.apps.UsersConfig',
    'apps.pipeline.apps.PipelineConfig',
    'apps.nomenclature.apps.NomenclatureConfig',
    'apps.promotions.apps.PromotionsConfig',
    'apps.orders.apps.OrdersConfig'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'apps.orders.middleware.SessionHeaderMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.server.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": os.getenv("DB_NAME", "barbar_food"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "12"),
        "HOST": os.getenv("DB_HOST", "postgres_bar_bar"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

CORS_ORIGIN_WHITELIST = ('http://localhost:3000', 'http://barbarfood.com')


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "session",
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "access-control-allow-credentials",
    "access-control-allow-headers",
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3001',
    'http://barbarfood.com',
    'http://back.barbarfood.com',
]


#CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True




DEFAULT_LANGUAGE = Languages.RUSSIAN
LANGUAGE_CODE = 'ru'
TIME_ZONE = "Asia/Almaty"

USE_I18N = True
USE_L10N = True
USE_TZ = True

CORS_ORIGIN_WHITELIST = (
        'http://barbarfood.com',
        'http://back.barbarfood.com',
        'http://localhost:8000',
        'http://localhost:3001',
        )

#APPEND_SLASH=False

STATIC_URL = os.getenv("STATIC_URL", "/static/")
STATIC_ROOT = os.getenv("STATIC_ROOT", os.path.join(BASE_DIR, 'static'))
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]

MEDIA_URL = os.getenv("MEDIA_URL", "/media/")
MEDIA_ROOT = os.getenv("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "apps.users.authentication.JWTAuthentication"
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M",
    "DEFAULT_PAGINATION_CLASS": "apps.common.pagination.CustomPagination",
    "PAGE_SIZE": 100,
    'COERCE_DECIMAL_TO_STRING': False
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "TESTEST",
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("JWT",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}
