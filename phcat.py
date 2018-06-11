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
from lib.core.data import logger
from lib.core.common import checkSystemEnvironment
from lib.core.common import setPaths
from lib.core.common import loadRules
from lib.core.cmdline import cmdLineParse
from lib.core.scan import scan
from lib.core.exception import PhcatSystemNotSupportException
from lib.core.exception import PhcatCmdParserErrorException
from lib.core.exception import PhcatCoroutineErrorException

def modulePath():
    """
    return project path
    """
    return os.path.dirname(os.path.realpath(__file__))

def main(debug=False):
    try:
        checkSystemEnvironment()
        setPaths(modulePath())
        if not debug: cmdLineParse()
        loadRules()
        scan()

    except PhcatSystemNotSupportException:
        pass
    except PhcatCmdParserErrorException:
        pass
    except PhcatCoroutineErrorException:
        pass
    except KeyboardInterrupt:
        logger.warn("Keyboard interrupt")
        exit()

if __name__=="__main__":
    main()


