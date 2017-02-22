# -*- coding: utf-8 -*-

# !/usr/bin/python

# Filename: func_doc.py
# Author: jianglb-alibaba
# mail: 419331434@qq.com


import time
from datetime import datetime
from functools import wraps
def warps_less1sec(t):
    def deco(func):
        def _deco(*args,**kwargs):
            start = time.clock()
            func(*args,**kwargs)
            end = time.clock()
            if end - start > t:
                print 'bad'
            else:
                print 'goods'
        return _deco
    return deco

"""
结果说明 : datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
1 millisecond（秒） = 1000 microseconds（毫秒）
1 minute = 60 seconds
1 hour = 3600 seconds
1 week = 7 days
运行结果如下  ： ('func runed ', datetime.timedelta(0, 0, 35000))
"""

def log_time_delta(func):
    @wraps(func)
    def deco(*args,**kwargs):
        start = datetime.now()
        res = func(*args,**kwargs)
        end = datetime.now()
        delta = end - start
        print("func runed ", delta)
        return res
    return deco



def warps_delta():
    def deco(func):
        def _deco(*args,**kwargs):
            start = time.clock()
            func(*args,**kwargs)
            end = time.clock()
            result = end-start
            return result
        return _deco
    return deco
"""
超过1秒 报bad

"""
@log_time_delta
def myfunc(*args,**kwargs):
    for i in range(100000):
        pass

myfunc()