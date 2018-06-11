#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from gevent import monkey
monkey.patch_all()
from types import coroutine
from subprocess import check_output,Popen,PIPE
import asyncio,time
import gevent
from gevent.pool import Pool


def run_cmd(i):
    p = Popen(['ping', '127.0.0.1', '-c', '2'], stdout=PIPE, stderr=PIPE)
    result, error = p.communicate()
    print(result)
@coroutine
async def runCmd():
    p = Popen(['ping','127.0.0.1','-c','2'], stdout=PIPE, stderr=PIPE)
    result, error = yield p.communicate()
    print(result)
async def await_():
    r = runCmd()
    await r.asend(None)
async def await__():
    await await_()
now = time.time()
# loop = asyncio.get_event_loop()
# myfun_list = (await__() for i in range(10))
# loop.run_until_complete(asyncio.gather(*myfun_list))
# run(await__())
p=Pool(10)
p.map_async(run_cmd,[i for i in range(10)])
print(time.time()-now)


# 10.092294216156006
