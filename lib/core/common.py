#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import os
import platform
from lib.core.data import conf,logger,paths
from lib.core.enums import OS
from lib.core.exception import *

def checkSystemEnvironment():
    '''
    Phcat not support windows
    :return:
    '''
    system = platform.platform().lower()
    if OS.WINDOWS in system:
        logger.critical("Phcat Do Not Support Windows System For Now")
        raise PhcatSystemNotSupportException
    elif OS.LINUX in system:
        conf['os']=OS.LINUX
    elif OS.MACOS in system:
        conf['os']=OS.MACOS

def setPaths(rootPath):
    '''
    Phcat project paths
    :param rootPath:
    :return:
    '''
    paths.PHCAT_ROOT_PATH=rootPath

    paths.PHCAT_RULES_PATH=os.path.join(rootPath,'rules')
    paths.PHCAT_LOG_PATH=os.path.join(rootPath,'logs')
    paths.PHCAT_CONFIG_PATH=os.path.join(rootPath,'config')




