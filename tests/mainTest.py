#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from phcat import main
import os
from lib.core.data import options

if __name__=='__main__':
    options.extension=['php']
    options.language='php'
    options.target=os.path.abspath('program')
    main(debug=True)


