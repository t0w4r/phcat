#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
        module scan
        traversal file ->

'''
from lib.core.data import options,logger
from lib.core.utils import Traversal
from lib.core.common import getOsPath
from lib.core.grep import Grep

class Scanner(object):
    __slots__ = ('target','extension','sources')

    def __init__(self):
        self.target = options.target
        self.extension = options.extension
        if not getOsPath().isdir(self.target):
            logger.critical("target[{0}] is not a valid directory".format(self.target))
            exit()

    def grepFunc(self):
        Grep().run(self.target)

    def scan(self):
        pass



def scan():
    scanner = Scanner()
    # stage one
    # grep all files return all matched results
    scanner.grepFunc()
    # stage two

    # stage three

