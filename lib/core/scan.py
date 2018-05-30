#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
        module scan
        traversal file ->

'''
from thirdparty.cobra.utils import Tool

class Scanner(object):
    __slots__ = ['find','grep']

    def __init__(self):
        self.find = Tool().find
        self.grep = Tool().grep



