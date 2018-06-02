#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import os
import platform
from lib.core.enums import OS
from lib.core.exception import *
from lib.core.data import paths,rules,logger,conf,options
from json import loads,JSONDecodeError
from lib.core.utils import Traversal
from thirdparty.cobra.utils import Tool

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

    conf['grep'] = Tool().grep

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
    paths.PHCAT_TESTS_PATH = os.path.join(rootPath, 'tests')


def loadRules():
    language=options.language
    traversal=Traversal()
    logger.info("start to load [{0}] rules".format(language))
    dir = os.path.join(paths.PHCAT_RULES_PATH,language)
    if not os.path.isdir(dir):
        logger.critical("Only support PHP for now, may try '-l php'")
        exit()
    files = traversal.traversal(dir,'json')
    t=0
    try:
        for file in files:
            with open(file) as f:
                content = f.read()
                rule = loads(content)
                if rule['status']=='on':
                    t+=1
                    rules.update({rule['name']:rule})
    except JSONDecodeError:
        logger.critical("rules load error, parse json file error")
        exit()
    logger.info("total {0}/{1} rules loaded".format(t,len(files)))

def getOsPath():
    return os.path






