#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import argparse,os
from lib.core.exception import PhcatCmdParserErrorException
from lib.core.data import options,logger


def cmdLineParse():
    parser = argparse.ArgumentParser(description='Phcat -- a php code analysis tool')

    cli = parser.add_argument_group('cli')
    cli.add_argument('-t','--target',dest="target",help="setup target to scan")
    cli.add_argument('-l','--language',
                     dest="language",
                     default="php",
                     help="setup program language")
    cli.add_argument('-e', '--extension',
                     dest="extension",
                     default="php",
                     help="setup program files' extension, like php,php3,php4")

    future = parser.add_argument_group("FUTURE")
    future.add_argument('--framework',
                        default="none",
                        dest='framework',help='setup project framework '
                                        'like thinkphp, ci and so on')
    args=parser.parse_args()
    checkArgs(args,parser)
    options.target = args.target
    options.language = args.language
    options.extension = [args.extension] if ',' not in args.extension else args.extension.split(',')
    options.framework = args.framework

def checkArgs(args,parser):
    if not args.target:
        parser.print_usage()
        logger.critical("please set target")
        raise PhcatCmdParserErrorException
    args.target=os.path.abspath(args.target)
    if not os.path.exists(args.target):
        logger.critical("the target is not exist")
        raise PhcatCmdParserErrorException
