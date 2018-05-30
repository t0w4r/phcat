#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import argparse
from lib.core.exception import PhcatCmdParserErrorException
from lib.core.data import options


def cmdLineParse():
    parser = argparse.ArgumentParser(description='Phcat -- a php code analysis tool')

    cli = parser.add_argument_group('cli')
    cli.add_argument('-t','--target',dest="target",help="setup target to scan")
    cli.add_argument('-e','--extension',
                     dest="extension",
                     default="php",
                     help="setup program language")

    future = parser.add_argument_group("FUTURE")
    future.add_argument('--framework',
                        default="none",
                        dest='framework',help='setup project framework '
                                        'like thinkphp, ci and so on')
    args=parser.parse_args()
    if not args.target:
        parser.print_help()
        raise PhcatCmdParserErrorException
    options.target = args.target
    options.extension = args.extension
    options.framework = args.framework



