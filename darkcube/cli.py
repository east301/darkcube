#!/usr/bin/env python
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
# darkcube CLI
#

import os
import sys

from django.core.management import execute_from_command_line


def main():
    # configures python path
    if os.path.exists('/etc/darkcube/darkcube_settings.py'):
        sys.path.insert(0, '/etc/darkcube')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'darkcube_settings')

    # runs CLI
    execute_from_command_line(sys.argv)
