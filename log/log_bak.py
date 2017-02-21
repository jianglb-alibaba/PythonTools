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

class LOG():

    def __init__(self):
        pass

    """
       此函数使用与出现可选参数时候，进行参数内容和个数的校验

    """

    def Usage(self,content,**kwargs):
        kwargs_list =[]
        usage_text = """

        Something is WRONG!
        Please according to the following form :
        For example:
        log2file("test",level=1)  指定日志的模式,其中 0--notset 1--debug 2--info 3--warning 4--error 5--critical，默认日志名称log.log
        or
        log2file("test",level=1,filename="log.log") 指定日志的模式和日志文件的名称和格式
        or
        log2file("test",filename="log.log") 指定日志文件的名称和格式，默认的日志模式为info，即level=2
        以上函数中"test"为日志消息内容，可以自定义为其他
        """
        logMsgNull = """
        Something is WRONG!
        The log message must not be NULL or None!
        For example :
        log2file("",filename="log.log") is forbidden. 必须在第一个双引号的地方输入日志内容，或者引用其他文本变量

        """
        num_kwargs =0
        ERROR_EXIT =99
        if content is None or content.strip()=='':
            print(logMsgNull.decode("utf-8").encode("gbk"))

            return
        if (len(kwargs) >2  ):
            print("the argument number is too long ,most requied 2 ( more than 2 is given)")
            num_kwargs = 3
            return num_kwargs
        elif (len(kwargs)==0):
            num_kwargs = 0
            return num_kwargs

        else:
            print(kwargs)
            if ( kwargs.has_key("level") and kwargs.has_key("filename") ) :
                # print(usage_text.decode("utf-8").encode("gbk"))
                num_kwargs =2
                return num_kwargs
            elif ( kwargs.has_key("level") or kwargs.has_key("filename")):
                num_kwargs =1
            else:
                print(usage_text.decode("utf-8").encode("gbk"))
                return ERROR_EXIT


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
    def format(self,*_level,*_filename,_log_format):
        if (_level )
        if (_log_format =="A"):
            self.logging.basicConfig(level=_level,
                                # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                format='%(asctime)s  %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename=_filename,
                                filemode='a')
        elif(_log_format =="B"):
            self.logging.basicConfig(level=_level,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename=_filename,
                                filemode='a')
        elif (_log_format =="C"):
            self.logging.basicConfig(level=_level,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename=_filename,
                                filemode='a')
        else:
            self.logging.basicConfig(level=_level,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename=_filename,
                                filemode='a')

    def log2file(self,content,*args,**kwargs):
        """
        result = 0  : 没有可选参数，默认
        result =1  : 有一个可选参数
        result = 2 : 有两个可选参数
        result =3 : 报错： 出现了三个可选，直接跳出
        result = 99 : 有一个到两个参数，其中一个参数的格式是错误的
        """
        _log_format = ""
        result = self.Usage(content,**kwargs)
        if (args =="A" or args =="a"):
            _log_format =="A"
        elif (args =="B" or args =="b"):
            _log_format =="B"
        elif (args =="C" or args =="b"):
            _log_format =="C"
        else:
            _log_format =="D"

        level = logging.INFO
        filename = "log.log"
        if (result==0):
            pass
        elif (result==1):
            if (kwargs.has_key(level)):
                level = kwargs["level"]
                self.format(level,filename,_log_format)
                self.logging.debug(content)
            else:
                filename = kwargs["filename"]
                self.format(level,filename,_log_format)
                self.logging.debug(content)
        elif (result==2):
            level = kwargs["level"]
            filename = kwargs["filename"]
            self.format(level,filename,_log_format)
            self.logging.debug(content)
        elif (result==3):
            return
        else:
            return

        # if (_loglevel == 0 ):
        #     _level =logging.NOTSET
        #     self.cid = 0
        # elif (_loglevel == 1 ):
        #     _level =logging.DEBUG
        #     self.cid = 1
        # elif (_loglevel == 2):
        #     _level = logging.INFO
        #     self.cid = 2
        # elif (_loglevel ==3):
        #     _level = logging.WARNING
        #     self.cid = 3
        # elif (_loglevel==4):
        #     _level = logging.ERROR
        #     self. cid = 4
        # elif(_loglevel==5):
        #     _level = logging.CRITICAL
        #     self.cid = 5
        # else:
        #     _level=logging.INFO
        #     self.cid = 6
        # # 获得系统默认编码格式
        # sysCharType = sys.getfilesystemencoding()
        # __file_content = _filecontent.decode("utf-8").encode("gbk")
        # __file_nothing = "(now is warning,it can be debug,error,critical )"
        # # __file_content = _filecontent.decode('gbk').encode('utf-8')
        logging.basicConfig(level=_level,
                            # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            format='%(asctime)s  %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=_filename,
                            filemode='a')
        # if (self.cid==0):  print("0")
        # elif (self.cid==1):print("1") ;logging.debug(__file_content)
        # elif (self.cid==2):print("2");logging.info(__file_content)
        # elif (self.cid==3):print("3");logging.warning(__file_content)
        # elif (self.cid==4):print("4");logging.error(__file_content)
        # elif (self.cid==5):print("5");logging.critical(__file_content)
        # elif (self.cid==6):print("other");logging.info(__file_nothing.decode("utf-8").encode("gbk")+"  "+__file_content)
        # else: pass



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
        # log.log2file(1,"log.log","大家好111")
        # log.log2file("test.log","大家好111")
        log.log2file("打算的撒")
        # content1 = "hello 大家好 "