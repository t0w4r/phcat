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
import os
from types import coroutine
import time
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
now=time.time()
rulePath="/Users/wh1t3p1g/Documents/Code/pythonProject/phcat/rules/php"
files=os.listdir(rulePath)
filepaths=[]
for file in files:
    filepaths.append(os.path.join(rulePath,file))
for file in filepaths:
    with open(file) as f:
        ret=json.loads(f.read())
        kb.update({ret['description']: ret})
# tasks=[loadRule(fp) for fp in filepaths]
# Coroutine().run(tasks)
print(kb)

print(time.time()-now)

# 0.0015523433685302734
# 0.0005271434783935547