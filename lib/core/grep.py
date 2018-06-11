#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
        use grep
'''

from lib.core.data import options,logger,conf
import subprocess




class Grep(object):
    __slots__ = ('target')

    def __init__(self):
        pass
    @staticmethod
    def run(rule):
        '''
        use system command from cobra
        :param target:
        :return:
        '''
        filters = []
        for e in options.extension:
            filters.append('--include=*.' + e)
        explode_dirs = ['.svn', '.cvs', '.hg', '.git', '.bzr','.idea']
        for explode_dir in explode_dirs:
            filters.append('--exclude-dir={0}'.format(explode_dir))

        # -s Suppress error messages / -n Show Line number / -r Recursive / -E regular expression
        param = [conf.grep, "-s", "-n", "-r", "-E"] + filters + [rule, options.target]
        try:
            p = subprocess.Popen(param, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result, error = p.communicate()

            return result.decode('utf-8').split(';\n')[:-1]
        except Exception as e:
            logger.critical('match exception ({e})'.format(e=e))
            return None