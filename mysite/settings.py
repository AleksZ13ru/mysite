"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y*x_u@x@#iq0*-x%t$f=0+_(^@j1zx271@ng_g=9m38*8nukho'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dept',
    'docx',
    'daybook',
    'si8device',
    'si8parsing',
    'easy_thumbnails',
    'filer',
    'mptt'

    # 'django_celery_results',
    # 'chartjs',
    # 'require'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'post1234',
        #'HOST': '35.163.174.99',  # Set to empty string for localhost.
        'HOST': 'localhost',  # Set to empty string for localhost.
        'PORT': '5432',  # Set to empty string for default.
    }
}


# Celery settings

CELERY_BROKER_URL = 'redis://localhost:6379/0'

# backend='redis://localhost', broker='redis://localhost'
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
# CELERY_BROKER_URL = 'redis://localhost'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # - для указания папки при разворачивании сервера
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = '/home/ubuntu/filermedia/media'

FILER_ENABLE_PERMISSIONS = True  # в админ. панели появляются настройки доступа к папкам
FILER_IS_PUBLIC_DEFAULT = False  # помещает файлы в приватную папку: smedia/filer_private

# FILER_STORAGES = {
#     'public': {
#         'main': {
#             'ENGINE': 'filer.storage.PublicFileSystemStorage',
#             'OPTIONS': {
#                 'location': '/home/ubuntu/mysite/media/filer',
#                 'base_url': '/media/filer/',
#             },
#             'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
#             'UPLOAD_TO_PREFIX': 'filer_public',
#         },
#         'thumbnails': {
#             'ENGINE': 'filer.storage.PublicFileSystemStorage',
#             'OPTIONS': {
#                 'location': '/home/ubuntu/mysite/media/filer_thumbnails',
#                 'base_url': '/media/filer_thumbnails/',
#             },
#         },
#     },
#     'private': {
#         'main': {
#             'ENGINE': 'filer.storage.PrivateFileSystemStorage',
#             'OPTIONS': {
#                 'location': '/home/ubuntu/mysite/smedia/filer',
#                 'base_url': '/smedia/filer/',
#             },
#             'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
#             'UPLOAD_TO_PREFIX': 'filer_private',
#         },
#         'thumbnails': {
#             'ENGINE': 'filer.storage.PrivateFileSystemStorage',
#             'OPTIONS': {
#                 'location': '/home/ubuntu/mysite/smedia/filer_thumbnails',
#                 'base_url': '/smedia/filer_thumbnails/',
#             },
#         },
#     },
# }
#
# FILER_SERVERS = {
#     'private': {
#         'main': {
#             'ENGINE': 'filer.server.backends.nginx.NginxXAccelRedirectServer',
#             'OPTIONS': {
#                 'location': '/home/ubuntu/mysite/smedia/filer',
#                 'nginx_location': '/filer_private',
#             },
#         },
#         'thumbnails': {
#             'ENGINE': 'filer.server.backends.nginx.NginxXAccelRedirectServer',
#             'OPTIONS': {
#                 'location': '/home/ubuntu/mysite/smedia/filer_thumbnails',
#                 'nginx_location': '/filer_private_thumbnails',
#             },
#         },
#     },
# }
