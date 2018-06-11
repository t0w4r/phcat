#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
        module scan
        traversal file ->

'''
from lib.core.data import options,logger,rules,kb
from lib.core.exception import PhcatCoroutineErrorException
from lib.core.grep import Grep
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool

class Scanner(object):
    __slots__ = ('target','pool')

    def __init__(self):
        pass



    def grepFunc(self):
        '''
        使用协程
        :return:
        '''
        def _grepFunc(data):
            ret = Grep().run(data[1])
            if ret:
                kb.regex.append({data[0]: ret})

        kb.regex=[] # init
        try:
            pool = Pool(options.threads)
            mapData = [(name,rule['regex']) for name,rule in rules.items()]
            pool.map(_grepFunc,mapData)
            print(kb.regex)
        except Exception:
            logger.critical("Coroutine Error")
            raise PhcatCoroutineErrorException

    def scan(self):
        pass



def scan():
    scanner = Scanner()
    # stage one
    # grep all files return all matched results
    scanner.grepFunc()
    # stage two

    # stage three

