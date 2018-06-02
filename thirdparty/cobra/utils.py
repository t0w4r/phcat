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
    __slots__ = ('grep')

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

        if 'darwin' == sys.platform:
            ggrep = ''
            for root, dir_names, file_names in os.walk('/usr/local/Cellar/grep'):
                for filename in file_names:
                    if 'ggrep' == filename or 'grep' == filename:
                        ggrep = os.path.join(root, filename)

            if ggrep == '':
                logger.critical("brew install grep pleases!")
                sys.exit(0)
            else:
                self.grep = ggrep
