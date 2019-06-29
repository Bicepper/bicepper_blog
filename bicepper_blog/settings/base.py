"""
Django settings for bicepper_blog project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
PROJECT_NAME = 'bicepper_blog'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e2_^%3g@u(ut3os00($=wtri8_-_u_to_c05jd_8tj$9o1b^xc'


# Gmail で送信する場合
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'muscleconsole@gmail.com'
EMAIL_HOST_PASSWORD = 'lbspwtnzezdltdpm'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Application definition
DJANGO_APPS = [
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

THIRD_PARTY_APPS = [
    'filebrowser',
    'imagekit',
    'froala_editor',
    'hitcount',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bicepper_blog.urls'

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
                'blog.context_processors.common',
            ],
        },
    },
]

WSGI_APPLICATION = 'bicepper_blog.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# dashboard
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# recaptcha info
GOOGLE_RECAPTCHA_SITE_KEY = '6LexaakUAAAAABFG1uWnMItmJ99da6TIX7G79Ftg'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LexaakUAAAAACa6WlvD98VLFFN4N_2geFTUvyf1'