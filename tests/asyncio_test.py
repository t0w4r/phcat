#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    phcat -- a php code analysis tool
    
    author:  wh1t3P1g <wh1t3P1g@gmail.com>
    description:
    
'''
from types import coroutine
from subprocess import check_output
def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value

@coroutine
async def async_generator_function():
    p=check_output(['ls'])
    yield p

async def async_function():
    g=async_generator_function()
    return await g.asend(None)


async def await_coroutine():
    result = await async_function()
    print(result)

# print(async_generator_function())
run(await_coroutine())

