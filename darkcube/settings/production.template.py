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

from darkcube.settings.common import *  # NOQA


# ================================================================================
# security
# ================================================================================

DEBUG = False    # NOTE: debug mode must be disabled in production environment
SECRET_KEY = 'spx4sm*9(8*$w8a!s-*$p$6=w001_z+$*3##s!eig1(-rnjzvj'


# ================================================================================
# database
#
# References:
#   * https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'darkcube',
        'USER': 'darkcube',
        'PASSWORD': 'darkcube',
        'HOST': '127.0.0.1',
        'PORT': '3306'
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
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211'
    }
}


# ================================================================================
# static files (CSS, JavaScript, Images)
#
# References:
#   * https://docs.djangoproject.com/en/1.9/howto/static-files/
# ================================================================================

STATIC_ROOT = '/opt/darkcube/static'


# ================================================================================
# Celery
#
# References:
#   * http://docs.celeryproject.org/en/master/getting-started/index.html
# ================================================================================

BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = BROKER_URL
