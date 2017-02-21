# -*- coding:utf-8 -*-
# coding=utf-8
# encoding: utf-8

# !/usr/bin/python

# Filename: func_doc.py
# Author: jianglb-alibaba
# mail: 419331434@qq.com
"""
LIFO即Last in First Out,后进先出。与栈的类似
how to use : from pythontools.queue.LIFO import Base
"""

import Queue
from log.LOG import LOG

myqueue = Queue.Queue(maxsize=10)


class Base(object):
    """
    队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。
    """

    def __init__(self, maxsize=1):
        self._maxsize = maxsize
        self._q = Queue.Queue(self._maxsize)
        self._log = LOG()

    """
    非堵塞写入队列，即设置put的参数block为false,同时进行队列满的异常捕获
    """

    def quickput(self, object):
        try:
            self._q.put(block=False)
        except Queue.Full as full:
            self._log.log2file()
