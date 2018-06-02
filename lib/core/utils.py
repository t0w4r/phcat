#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
        tools
'''

import os
from lib.core.enums import CUSTOM_TYPE

class Traversal(object):
    '''
    Traversal dirs
    '''
    __slots__ = ('exts','ret','basedir')

    def __init__(self):
        self.ret=[]

    def push(self,dir):
        if os.path.isdir(dir):
            return CUSTOM_TYPE.DIR
        elif os.path.isfile(dir):
            extension = os.path.basename(dir).split('.')[-1].lower()
            if extension in self.exts:
                self.ret.append(dir)
                return CUSTOM_TYPE.FILE

        return CUSTOM_TYPE.OTHER

    def _traversal(self,dir):
        if self.push(dir) == CUSTOM_TYPE.DIR:
            dirs = os.listdir(dir)
            for fp in dirs:
                fp = os.path.join(self.basedir,fp)
                if self.push(fp) == CUSTOM_TYPE.DIR:
                    self._traversal(fp)



    def traversal(self,dir,ext):
        '''
        :param dir: target directory
        :param ext: target file extension
        :return: filepath like /path/to/file.ext
        '''
        self.exts = ext
        self.basedir = dir
        self._traversal(dir)
        return self.ret