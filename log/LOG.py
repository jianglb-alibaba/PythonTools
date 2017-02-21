# -*- coding: utf-8 -*-

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
import sys

class LOG:

    """
    日志级别有:  CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    参数解释 ：
    _loglevel = 0:  NOTSET
    _loglevel = 1; DEBUG
    _loglevel =2 : INFO
    _loglevel =3: WARNING
    _loglevel =4: ERROR
    _loglevel =5: CRITICAL

   how to use : log2file("debug","log.log","hello 大家好 ")
    a -- 添加模式
    w --添加覆盖模式

    """


    def log2file(self,_loglevel,_filename,_filecontent):
        if (_loglevel == 0 ):
            _level =logging.NOTSET
            self.cid = 0
        elif (_loglevel == 1 ):
            _level =logging.DEBUG
            self.cid = 1
        elif (_loglevel == 2):
            _level = logging.INFO
            self.cid = 2
        elif (_loglevel ==3):
            _level = logging.WARNING
            self.cid = 3
        elif (_loglevel==4):
            _level = logging.ERROR
            self. cid = 4
        elif(_loglevel==5):
            _level = logging.CRITICAL
            self.cid = 5
        else:
            _level=logging.DEBUG
            self.cid = 6
        # 获得系统默认编码格式
        sysCharType = sys.getfilesystemencoding()
        __file_content = _filecontent.decode("utf-8").encode("gbk")
        __file_nothing = "(日志模式不明确，系统按照Info模式记载日志)"
        # __file_content = _filecontent.decode('gbk').encode('utf-8')
        logging.basicConfig(level=_level,
                            # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            format='%(asctime)s  %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=_filename,
                            filemode='a')
        if (self.cid==0):  print("0")
        elif (self.cid==1):print("1") ;logging.debug(__file_content)
        elif (self.cid==2):print("2");logging.info(__file_content)
        elif (self.cid==3):print("3");logging.warning(__file_content)
        elif (self.cid==4):print("4");logging.error(__file_content)
        elif (self.cid==5):print("5");logging.critical(__file_content)
        elif (self.cid==6):print("other");logging.info(__file_nothing.decode("utf-8").encode("gbk")+"  "+__file_content)
        else: pass



    def log2all(self,filename="log.log"):
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


if __name__ == '__main__':
        log = LOG()
        log.log2file(1,"log.log","大家好111")
        # content1 = "hello 大家好 "