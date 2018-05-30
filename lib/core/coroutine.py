#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
import asyncio
from lib.core.data import kb
import json
from types import coroutine
import aiofiles

class Coroutine(object):
    __slots__=()

    def __init__(self):
        pass

    @classmethod
    async def _run(cls,tasks):
        dones, pendings = await asyncio.wait(tasks)
        for task in dones:
            ret=task.result()
            kb.update({ret['description']:ret})

    @classmethod
    def run(cls,tasks):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cls._run(tasks))
        loop.close()
@coroutine
async def async_fopen(filepath):
    with open(filepath) as f:
        yield f.read()


async def loadRule(filepath):
    async with aiofiles.open(filepath) as f:
        data = await f.read()
    return json.loads(data)