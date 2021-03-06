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
# Django settings for darkcube development project.
#
# References:
#   * https://docs.djangoproject.com/en/1.9/topics/settings/
#   * https://docs.djangoproject.com/en/1.9/ref/settings/
#   * https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
#

import os

from redislite import Redis

from .common import *   # NOQA


# ================================================================================
# security
# ================================================================================

DEBUG = True    # NOTE: debug mode must be disabled in production environment
SECRET_KEY = 'spx4sm*9(8*$w8a!s-*$p$6=w001_z+$*3##s!eig1(-rnjzvj'


# ================================================================================
# database
#
# References:
#   * https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'temporary', 'db.sqlite3'),
    }
}


# ================================================================================
# cache
#
# References:
#   * https://docs.djangoproject.com/ja/1.9/topics/cache/
# ================================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}


# ================================================================================
# static files (CSS, JavaScript, Images)
#
# References:
#   * https://docs.djangoproject.com/en/1.9/howto/static-files/
# ================================================================================

STATIC_ROOT = os.path.join(BASE_DIR, 'temporary', 'static')


# ================================================================================
# Celery
#
# References:
#   * http://docs.celeryproject.org/en/master/getting-started/index.html
# ================================================================================

CELERY_REDIS_PORT = os.environ.get('CELERY_REDIS_PORT', '8001')
CELERY_REDIS = Redis(
    os.path.join(BASE_DIR, 'temporary', 'celery.redis'),
    serverconfig={'port': CELERY_REDIS_PORT})

BROKER_URL = 'redis://127.0.0.1:{}/0'.format(CELERY_REDIS_PORT)
CELERY_RESULT_BACKEND = BROKER_URL
