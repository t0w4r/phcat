#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool

    author:  wh1t3P1g  <wh1t3P1g@gmail.com>
    description:
        phcat framework global data
'''

from lib.core.dataType import AttribDict

from lib.core.log import LOGGER

# project paths
paths = AttribDict()
# cmd options
options = AttribDict()
# config dict
conf = AttribDict()
# rules
rules = AttribDict()
# results
kb = AttribDict()
# logger
logger = LOGGER

