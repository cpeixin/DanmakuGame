#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 4:07 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : processJoin.py
# @Description:
from multiprocessing import Process
import os
import time


def run_proc(name):
    time.sleep(3)
    print('Run child process %s (%s)...' % (name, os.getpid()))


def hello_world():
    # time.sleep(5)
    time.sleep(5)
    print('hello world!')
    print('Run child process (%s)...' % (os.getpid()))


if __name__ == '__main__':
    print ('Parent process %s.' % os.getpid())
    p1 = Process(target=run_proc, args=('test',))
    p2 = Process(target=hello_world)
    print('Process will start.')
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
    print('Process end.')