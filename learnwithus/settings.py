"""
Django settings for learnwithus project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""


# from chatgpt for custom user
AUTH_USER_MODEL = 'component.CustomUser'


from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$dft(fj@wrz0c10^@0*b*#(n&ed^6y(+p@*_&mdqwcjl=$*xww"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['.vercel.app','.now.sh','127.0.0.1','localhost']
# ALLOWED_HOSTS = ['www.learnwithus.org.in','learnwithus.org.in','ec2-16-16-220-198.eu-north-1.compute.amazonaws.com','ip-172-31-5-103.eu-north-1.compute.internal','ec2amaz-iakr70o.eu-north-1.compute.internal','127.0.0.1','172.31.5.103','16.16.220.198']

ALLOWED_HOSTS = [
    'www.learnwithus.org.in',
    'learnwithus.org.in',
    'ec2-16-16-220-198.eu-north-1.compute.amazonaws.com',
    'ip-172-31-5-103.eu-north-1.compute.internal',
    'ec2amaz-iakr70o.eu-north-1.compute.internal',
    '127.0.0.1',
    '172.31.5.103',
    '16.16.220.198',
    # '192.168.121.180' # for my local development
]


# Application definition

INSTALLED_APPS = [
    # 'component',
    'component.apps.MyAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]


AUTH_USER_MODEL = 'component.CustomUser'

# Application definition
SITE_ID = 1



SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE":[
            "profile",
            "email"
        ],
        "AUTH_PARAMS":{
            'access_type':'online'
        }
        
    }
}




MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "component.middleware.UserActivityMiddleware",
]

ROOT_URLCONF = "learnwithus.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "learnwithus.wsgi.application"





# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'anuragfx818@gmail.com'
EMAIL_HOST_PASSWORD = 'ycfxfnaerstmfjnl'
DEFAULT_FROM_EMAIL = 'anuragfx818@gmail.com'








# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# railway
# DATABASES = {
#     'default':{
#         "ENGINE":"django.db.backends.postgresql",
#         "NAME":'railway',
#         "USER":'postgres',
#         'PASSWORD':'UinbkcXWLRHOEiTRXhjTkJumhgqRvjCh',
#         'HOST':'viaduct.proxy.rlwy.net',
#         'PORT':'34452'

#     }
# }

# Azure database

# DATABASES = {
#     'default':{
#         "ENGINE":"django.db.backends.postgresql",
#         "NAME":'postgres',
#         "USER":'fx818',
#         'PASSWORD':'@Anurag818@',
#         'HOST':'learnwithus.postgres.database.azure.com',
#         'PORT':'5432'

#     }
# }







# AWS Databases
# DATABASES = {
#     'default':{
#         "ENGINE":"django.db.backends.postgresql",
#         "NAME":'learnwithusdb',
#         "USER":'learnwithusdb',
#         'PASSWORD':'learnwithus818',
#         'HOST':'learnwithusdb.c1eaw826wdev.eu-north-1.rds.amazonaws.com',
#         'PORT':'5432'
#     }
# }


# Using Supabase
# DATABASES = {
#     'default':{
#         "ENGINE":"django.db.backends.postgresql",
#         "NAME":'postgres',
#         "USER":'postgres.mvaonazvlarpgxcrjpsp',
#         'PASSWORD':'@learnwithus818@',
#         'HOST':'aws-0-ap-south-1.pooler.supabase.com',
#         'PORT':'5432'
#     }
# }







# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# STATIC_URL = "static/"
# STATICFILES_DIRS = os.path.join(BASE_DIR,'static'),
# STATIC_ROOT = os.path.join(BASE_DIR,' staticfiles_build', 'static')



STATIC_URL = 'static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR , 'static'),)  # Note the comma at the end of the line

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')  # Remove the space before 'staticfiles_build'


# From code dev community
# STATICFILES_DIRS = [BASE_DIR/'static',]
# STATIC_ROOT = BASE_DIR/'staticfiles'


# from Django doc
# https://forum.djangoproject.com/t/having-troubles-with-django-project-on-deployment-on-vercel/24269/33
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# MEDIA_URL = 'img/'
# MEDIA_ROOT = BASE_DIR/'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# from chatgpt for custom user
AUTH_USER_MODEL = 'component.CustomUser'



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'