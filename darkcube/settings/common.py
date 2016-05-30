#
# DarkCube
# Copyright 2016 DarkCube developers
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
#
# =====
# Django settings for darkcube project.
#
# References:
#   * https://docs.djangoproject.com/en/1.9/topics/settings/
#   * https://docs.djangoproject.com/en/1.9/ref/settings/
#   * https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
#

import os

# ================================================================================
# project directory
# ================================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ================================================================================
# security
# ================================================================================

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

ALLOWED_HOSTS = ['*']


# ================================================================================
# Django apps & middlewares
# ================================================================================

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party apps
    'compressor',
    'crispy_forms',

    # darkcube apps
    'darkcube.apps.common',
    'darkcube.apps.vendor',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]


# ================================================================================
# URL routing
# ================================================================================

ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'darkcube.urls'

WSGI_APPLICATION = 'darkcube.wsgi.application'


# ================================================================================
# template
# ================================================================================

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
            ]
        }
    }
]


# ================================================================================
# internationalization
#
# References:
#   * https://docs.djangoproject.com/en/1.9/topics/i18n/
# ================================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ================================================================================
# static files (CSS, JavaScript, Images)
#
# References:
#   * https://docs.djangoproject.com/en/1.9/howto/static-files/
# ================================================================================

STATIC_URL = '/static/'


# ================================================================================
# Celery
#
# References:
#   * http://docs.celeryproject.org/en/master/getting-started/index.html
# ================================================================================

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
