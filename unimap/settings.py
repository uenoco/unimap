"""
Django settings for unimap project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# dajngo-environ
env = environ.Env(DEBUG=(bool,True))
env.read_env(os.path.join(BASE_DIR,'.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

#CORS_ORIGIN_ALLOW_ALL = True #add for CROSCORS_ALLOW_CREDENTIALS = True
#CORS_ALLOW_HEADERS = ['*']
CORS_ALLOWED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1', 'https://unimap-staging.zukatech.com' ]
#CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'https://unimap-staging.zukatech.com' ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    ## django-geojson
    'djgeojson',
    ## django-allauth
    #'django.contrib.sites',
    #'allauth.account',
    #'allauth.socialaccount',    # ソーシャル連携認証なしでも必要',
    'import_export',
    # unimap Applicaition
    'unimap',
    #CORS
    'corsheaders',
    # restAPI
    'rest_framework',
    'rest_framework_gis',
    # django-dbbackup
    'dbbackup',
    # django-cleanup
    'django_cleanup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #add for CROS
    'corsheaders.middleware.CorsMiddleware', 
    #
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'unimap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                # 'django.template.context_processors.request',
                # GOOGLE ANALYTICS
                'unimap.context_processors.google_analytics',
            ],
        },
    },
]

WSGI_APPLICATION = 'unimap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
    'default': {
        'ENGINE': env.get_value('DATABASE_ENGINE', default='django.contrib.gis.db.backends.postgis'),
        'NAME': env.get_value('DATABASE_NAME', default='unimap'),
        'USER': env.get_value('DATABASE_USER', default='unimap'),
        'PASSWORD': env.get_value('DATABASE_PASSWORD', default='unimap00'),
        'HOST': env.get_value('DATABASE_HOST', default='localhost'),
        'PORT': env.get_value('DATABASE_PORT', default='5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),  # プロジェクト直下のstaticディレクトリを指定
)

# Add for wsgi with Apache
STATIC_ROOT = os.path.join(BASE_DIR, 'deploy')  # プロジェクト直下のdeployディレクトリを指定

# MEDIA_ROOT for models.ImageField
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#ログ出力先のディレクトリを設定する
#LOG_BASE_DIR = os.path.join("/var", "log", "app")
LOG_BASE_DIR = os.path.join( BASE_DIR, "log" )
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(asctime)s [%(levelname)s] %(message)s"}},
    "handlers": {
        "info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_BASE_DIR, "info.log"),
            "formatter": "simple",
        },
        "warning": {
            "level": "WARNING",
            "class": "logging.FileHandler",
           "filename": os.path.join(LOG_BASE_DIR, "warning.log"),
          "formatter": "simple",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_BASE_DIR, "error.log"),
            "formatter": "simple",
        },
        "console": {
            "level": 'DEBUG',
            "class": 'logging.FileHandler',
            "filename": os.path.join(LOG_BASE_DIR, "debug.log"),
            "formatter": "simple",
        },
    },
    "root": {
        #"handlers": ["info", "warning", "error"],
        "handlers": ["error"],
        "level": "WARNING",
    },
}

# django-dbbackup
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'backup')}


# GOOGLE ANALYTICS ID 
GOOGLE_ANALYTICS_ID = env('GOOGLE_ANALYTICS_ID')
