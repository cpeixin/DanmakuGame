# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 2:04 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : threadDemo.py
# @Description: 多线程


import _thread
import threading
import time


def _thread_demo():
    # 为线程定义一个函数
    def print_time(threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % (threadName, time.ctime(time.time())))

    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2,))
        _thread.start_new_thread(print_time, ("Thread-2", 4,))
    except:
        print("Error: 无法启动线程")

    while 1:
        pass


def threading_demo():
    exitFlag = 0

    class myThread(threading.Thread):
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay

        def run(self):
            print("开始线程：" + self.name)
            print_time(self.name, self.delay, 5)
            print("退出线程：" + self.name)

    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")


if __name__ == '__main__':
    threading_demo()
