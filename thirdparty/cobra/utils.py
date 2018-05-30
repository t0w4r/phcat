#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import os,sys
from lib.core.data import logger

class Tool:
    def __init__(self):

        # `grep` (`ggrep` on Mac)
        if os.path.isfile('/bin/grep'):
            self.grep = '/bin/grep'
        elif os.path.isfile('/usr/bin/grep'):
            self.grep = '/usr/bin/grep'
        elif os.path.isfile('/usr/local/bin/grep'):
            self.grep = '/usr/local/bin/grep'
        else:
            self.grep = 'grep'

        # `find` (`gfind` on Mac)
        if os.path.isfile('/bin/find'):
            self.find = '/bin/find'
        elif os.path.isfile('/usr/bin/find'):
            self.find = '/usr/bin/find'
        elif os.path.isfile('/usr/local/bin/find'):
            self.find = '/usr/local/bin/find'
        else:
            self.find = 'find'

        if 'darwin' == sys.platform:
            ggrep = ''
            gfind = ''
            for root, dir_names, file_names in os.walk('/usr/local/Cellar/grep'):
                for filename in file_names:
                    if 'ggrep' == filename or 'grep' == filename:
                        ggrep = os.path.join(root, filename)
            for root, dir_names, file_names in os.walk('/usr/local/Cellar/findutils'):
                for filename in file_names:
                    if 'gfind' == filename:
                        gfind = os.path.join(root, filename)
            if ggrep == '':
                logger.critical("brew install grep pleases!")
                sys.exit(0)
            else:
                self.grep = ggrep
            if gfind == '':
                logger.critical("brew install findutils pleases!")
                sys.exit(0)
            else:
                self.find = gfind