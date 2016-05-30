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
# darkcube URL configuration
#
# References:
#   * https://docs.djangoproject.com/en/1.9/topics/http/urls/
#

from django.conf import settings
from django.conf.urls import url


# ================================================================================
# default URL patterns
# ================================================================================

urlpatterns = [
    # TODO: add your own URL patterns
]


# ================================================================================
# Activates Django admin URL patterns only when DEBUG mode
# ================================================================================

if settings.DEBUG:
    from django.contrib import admin

    urlpatterns += [
        url(r'^admin/', admin.site.urls),
    ]
