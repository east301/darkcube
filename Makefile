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

# ================================================================================
# configurations
# ================================================================================

SETTINGS := darkcube.settings.development

SERVER_ADDRESS := 0.0.0.0
SERVER_PORT := 8000

CELERY_REDIS_PORT := 8001
CELERY_OPTIONS := --app darkcube --loglevel DEBUG --no-color
CELERY_WORKER_OPTIONS := --concurrency 1
CELERY_BEAT_OPTIONS :=


# ================================================================================
# setup
# ================================================================================

install-python-dependencies:
	pip install -r requirements/common.txt
	pip install -r requirements/development.txt

install-node-dependencies:
	npm install

install-dependencies: install-python-dependencies install-node-dependencies


# ================================================================================
# server
# ================================================================================

make-migration:
	python manage.py makemigration --noinput

migrate:
	python manage.py migrate --noinput

run-server:
	python manage.py runserver ${SERVER_ADDRESS}:${SERVER_PORT}

run-celery-worker:
	DJANGO_SETTINGS_MODULE=${SETTINGS} CELERY_REDIS_PORT=${CELERY_REDIS_PORT}\
		celery worker ${CELERY_OPTIONS} ${CELERY_WORKER_OPTIONS}

run-celery-beat:
	DJANGO_SETTINGS_MODULE=${SETTINGS} CELERY_REDIS_PORT=${CELERY_REDIS_PORT}\
		celery beat ${CELERY_OPTIONS} ${CELERY_BEAT_OPTIONS}


# ================================================================================
# test & lint
# ================================================================================

run-tests:
	py.test

run-lint:
	flake8
