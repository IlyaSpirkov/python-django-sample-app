import locale
import os
from pathlib import Path

from dj_database_url import parse as uri

from django.utils import timezone
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

PROJECT = "sample"
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "PLEASE_ENTER_SECRET_KEY")
DEBUG = os.environ.get("DEBUG", False)
ALLOWED_HOSTS = ["0.0.0.0", "*", "localhost"]

PROJECT_APPS = [
    "account",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
] + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sample.urls"
APPEND_SLASH = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / PROJECT / "templates/admin/"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sample.wsgi.application"

# DATABASES = {"default": uri(os.environ.get("DB_URI"), engine="django_db_geventpool.backends.postgresql_psycopg2")}
# DATABASES = {"default": uri("postgres://sample:sample@db:5432/sample", engine=None)}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8}
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = "ru-RU"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

DATE_FORMAT = "%d.%m.%Y"
TIME_FORMAT = "%H:%M:%S"

STATIC_URL = "/admin/static/"
STATIC_ROOT = BASE_DIR / PROJECT / "files" / "static"

MEDIA_URL = "/admin/media/"
MEDIA_ROOT = BASE_DIR / PROJECT / "files" / "media"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

AUTH_USER_MODEL = "account.User"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "sample.pagination.Pagination",
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DATE_INPUT_FORMATS": ["iso-8601"],
}

SPECTACULAR_SETTINGS = {
    'COMPONENT_SPLIT_REQUEST': True
}

REDIS_DEFAULT_CACHE_URI = os.environ.get("REDIS_DEFAULT_CACHE_URI", "redis://redis:6379/1")
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_DEFAULT_CACHE_URI,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timezone.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timezone.timedelta(weeks=2),
}


CELERY_BROKER_URL = os.environ.get("BROKER_URI")
CELERY_RESULT_BACKEND = os.environ.get("BROKER_URI")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# AWS settings
BUCKET_NAME = 'sample'
BUCKET_DIR = 'avatars/'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")


# LOGGING = LOGGING

if sentry_dsn := os.environ.get("SENTRY_DSN", ""):
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[DjangoIntegration(), RedisIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
