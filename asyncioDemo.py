#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 4:28 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : asyncioDemo.py
# @Description:

import asyncio


async def run():
    print('Running ...')
    await asyncio.sleep(2)
    print('... Over!')


async def main():
    print('Hello ...')
    await asyncio.sleep(3)
    print('... World!')


asyncio.run(main())
asyncio.run(run())
