#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
        phcat framework exceptions
'''

class PhcatBaseException(Exception):
    pass

class PhcatFilepathException(PhcatBaseException):
    pass

class PhcatSystemNotSupportException(PhcatBaseException):
    pass

class PhcatCmdParserErrorException(PhcatBaseException):
    pass

class PhcatCoroutineErrorException(PhcatBaseException):
    pass