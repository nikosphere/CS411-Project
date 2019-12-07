"""
Django settings for CS411_Project_V1 project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kz-o7fvt--(o@ivo1h11mqxz)#r1zb0bw4*-0#@-&9(wcg3ead'
YELP_APP_ID = config("YELP_APP_ID", default='')
YELP_APP_KEY = config("YELP_APP_KEY", default='')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Redirect User Post-Authentication
LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/trends/yelp'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/'

#SOCIAL AUTH URL
SOCIAL_AUTH_URL_NAMESPACE = 'Trends:social'

#google OAuth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '845240979934-v93tsvh1e6gv7oi7j7do7bc1ot084oca.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'WzvHzUBMHnl-wVm0ryrbE4a_'

#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'Trends.apps.TrendsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'loadjson',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'CS411_Project_V1.urls'


AUTHENTICATION_BACKENDS = [
        'social_core.backends.instagram.InstagramOAuth2',
        'social_core.backends.facebook.FacebookOAuth2',
        'social_core.backends.google.GoogleOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    ]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'CS411_Project_V1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
