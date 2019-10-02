
##
## Copyright 2015 Mostafa Sedaghat Joo
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
##


#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse


def utf8_to_cp1256(filename):
    with open(filename, 'r', encoding='utf-8') as readfile:
        text = readfile.read()

        # persian ye
        text = text.replace(u'\u06cc', u'\u064a')

        # persian k
        text = text.replace(u'\u06a9', u'\u0643')

        text = text.encode('cp1256')

        with open(filename + ".cp1256", 'wb') as writefile:
            writefile.write(text)


def cp1256_to_utf8(filename):
    with open(filename, 'r', encoding='cp1256') as readfile:
        text = readfile.read()

        # persian ye
        text = text.replace(u'\u064a', u'\u06cc')

        # persian k
        text = text.replace(u'\u0643', u'\u06a9')

        with open(filename + ".ut8", 'w') as writefile:
            writefile.write(text)


