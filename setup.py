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

import os
from setuptools import find_packages, setup


# ================================================================================
# helpers
# ================================================================================

def read_file(*args):
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, *args)
    with open(path) as fin:
        return fin.read()


# ================================================================================
# run setup
# ================================================================================

setup(
    # package information
    name='darkcube',
    version='0.0.0',
    description='DarkCube',
    long_description='DarkCube',
    license='Apache-2.0',
    url='https://github.com/east301/darkcube',
    author='DarkCube developers',
    author_email='me@east301.net',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='reference manager',

    # package data
    packages=find_packages(exclude=['requirements', 'tests']),
    install_requires=read_file('requirements', 'common.txt').splitlines(),

    # CLI
    entry_points={
        'console_scripts': [
            'darkcube-cli=darkcube.cli:main'
        ]
    },
)
