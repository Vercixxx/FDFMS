from pathlib import Path
import os
import json
from datetime import timedelta


SECRET_DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'secret_data.json')

with open(SECRET_DATA_FILE) as f:
    secret_data = json.load(f)

BASE_DIR = Path(__file__).resolve().parent.parent



# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = secret_data.get("SECRET_KEY_VALUE")



DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
# ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    # My apps
    'users',
    'payroll_dept',
    'hr_dept',
    'asset_dept',
    'clients_dept',
    'car',
    'restaurant',
    'rest_manager',
    'driver',
    'administrator',
    'fleet',
    'posts',
    
    # My packages
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'djoser',
    'corsheaders',
    
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    
]

# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
    "http://192.168.0.155:8080",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': secret_data.get("DB_NAME"),
        'USER': secret_data.get("DB_USER"),
        'PASSWORD': secret_data.get("DB_PASSWORD"),
        'HOST': secret_data.get("DB_HOST"),
        'PORT': secret_data.get("DB_PORT"),
    }
}


# Password validation

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

# User
AUTH_USER_MODEL = 'users.GeneralUser'


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Ustaw czas ważności tokena dostępu
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Ustaw czas ważności odświeżania tokena
    # 'SLIDING_TOKEN_LIFETIME': timedelta(days=14),  # Ustaw czas ważności slidinowego tokena
    # 'SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD': timedelta(days=7),  # Ustaw okres łaski przed odświeżeniem slidinowego tokenu
    # 'ROTATE_REFRESH_TOKENS': False,
    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': None,
    # 'VERIFYING_KEY': None,
    # "AUTH_HEADER_TYPES": ("Bearer",),
    # "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    
    
    # "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    # "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME_ALLOW_REFRESH': True,
    'SLIDING_TOKEN_LIFETIME_ALLOW_REFRESH': True,
    'SLIDING_TOKEN_REFRESH_EACH_TIME': True,
    'SLIDING_TOKEN_REFRESH_AFTER_GRACE_PERIOD': False,
    
}