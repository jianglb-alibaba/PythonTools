# -*- coding:utf-8 -*-
# coding=utf-8
# encoding: utf-8

# !/usr/bin/python

# Filename: func_doc.py
# Author: jianglb-alibaba
# mail: 419331434@qq.com
"""
格式化日志输入:
Sun, 24 May 2009 21:48:54 demo2.py[line:11] DEBUG This is debug message


how to use :
"""

import logging


class LOG(object):
    def log2file(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='myapp.log',
                            filemode='w')

        logging.debug('This is debug message')
        logging.info('This is info message')
        logging.warning('This is warning message')


    def log2all(self):
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

        #################################################################################################
        #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        #################################################################################################

        logging.debug('This is debug message')
        logging.info('This is info message')
        logging.warning('This is warning message')