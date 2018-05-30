#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool

    author:  wh1t3P1g  <wh1t3P1g@gmail.com>
    description:
        phcat framework main entry

    only support linux or mac for now
'''
import os
from lib.core.common import checkSystemEnvironment
from lib.core.common import setPaths
from lib.core.cmdline import cmdLineParse
from lib.core.exception import PhcatSystemNotSupportException
from lib.core.exception import PhcatCmdParserErrorException

def modulePath():
    """
    return project path
    """
    return os.path.dirname(os.path.realpath(__file__))

def main():
    try:
        checkSystemEnvironment()
        setPaths(modulePath())
        cmdLineParse()


    except PhcatSystemNotSupportException:
        pass
    except PhcatCmdParserErrorException:
        pass

if __name__=="__main__":
    main()


