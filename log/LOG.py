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

    def check_kwargs(self, content, **kwargs):


        level_value = [1, 2, 3, 4, 5]
        format_value=['A','B','C','D','E']
        datefmt_value =['normal','easy','custom']
        filemode = ['a','w']
        arg_list = ['level','filename','format','datefmt','filemode']


        for key in kwargs:
                 if key not in arg_list:  # 以 arg_list里的参数规格为模板，检查参数列表里面是否存在正确的参数名字
                    print("""提供的参数名字不对,请检查,完整的log.log2file("test",level=5,format="*",datefmt=""*",filemode="*")""".decode('utf-8').encode('gbk'))
                    return
                 else:
                     pass



        print("核对参数名字正确后开始匹配参数的内容".decode('utf-8').encode('gbk'))



        if (kwargs.has_key('level')):
            if kwargs['level'] not in level_value:
                print("""level=value:  value must be  1 to 5 ,Check Again Please!
                         You can use log2file('help") to get help """)
                return


        if (kwargs.has_key('filename')):
            if (len(kwargs['filename'] ) >20):
                print("filename=value:  length of value must not exceed 20 charater ,Check Again Please!  You can use log2file_help() to get help ")
                return

        if (kwargs.has_key('format')):
            if kwargs['format'] not in format_value:
                print("format=value:  value must be  A to E (match upperlower case) ,Check Again Please! You can use log2file_help() to get help")
                return


        if (kwargs.has_key('datefmt')):
            if kwargs['datefmt'] not in datefmt_value:
                print("""datefmt=value:  value must be  normal,easy,custom (match upperlower case) ,Check Again Please!
                         You can use log2file('help") to get help""")
                return
        if (kwargs.has_key('filemode')):
            if kwargs['filemode'] not in filemode:
                print("""filemode=value:  value must be  a,w, (match upperlower case) ,Check Again Please!
                         You can use log2file('help") to get help""")
                return




    def log2file_help(self):
        usage_text = """
        log2file  Usage: (注意:以下内容区分大小写)
        1) log2file("msg"):日志内容为info,日志名称为log.log,日志
        2) log2file("msg",level=1,filename="log.logs",):
        3) log2file("msg",level=1,filename="log.logs"

        """
        if (help=="help" or help=="HELP"):
            print(usage_text.decode('gbk').encode('utf-8'))

        else:
            print("""Usage:
                        Please Use the follow command:
                        log2file("help")  or  log2file("HELP") """)
            return

    def log2file(self,content,**kwargs):
        """
        **kwargs:
        level =
        filename =
        format =
        datefmt =
        """
        _format_dict = {'A':'%(asctime)s  %(levelname)s %(message)s','B':'%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'}
        _datefmt_dict = {'normal':'%a, %d %b %Y %H:%M:%S','easy':'%Y-%b-%d %H:%M:%S','custom':'%Y-%m-%d %H:%M:%S'}
        if (len(kwargs)>5):
            print("可选参数超过5个(不含消息内容参数)，请检查".decode("utf-8").encode("gbk"))
            return
        nullcontent_warning = "消息内容不允许为空, 已退出程序，不执行后面命令"
        if (content.strip()==''):
            print(nullcontent_warning.decode("utf-8").encode("gbk"))
            return

        if (len(kwargs)==0): #默认情况记载日志：info模式记载，格式如下:
            logging.basicConfig(level=logging.INFO,
                                # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                format='%(asctime)s  %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename="log.log",
                                filemode='a')
            logging.info(content)
        else:
            self.check_kwargs(content,**kwargs)
            _level = kwargs["level"] if kwargs.has_key("level")  else  logging.INFO
            _filename = kwargs["filename"] if kwargs.has_key("filename")  else  "log.log"
            _format = kwargs["format"] if kwargs.has_key("format")  else "A"
            _datefmt = kwargs["datefmt"] if kwargs.has_key("datefmt")  else "normal"
            _filemode = kwargs["filemode"] if kwargs.has_key("filemode")  else "a"
            try:
                logging.basicConfig(level=_level,
                                    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                    format=_format_dict[_format],
                                    datefmt=_datefmt_dict[_datefmt],
                                    filename=_filename,
                                    filemode=_filemode)
            except Exception as e:
                print("Something is WRONG! 程序异常退出, 请参照Usage格式输入".decode("utf-8").encode("gbk"))
            else:
                if _level==1:logging.debug(content.decode("utf-8").encode("gbk"))
                elif _level==2:logging.info(content.decode("utf-8").encode("gbk"))
                elif _level==3:logging.warning(content.decode("utf-8").encode("gbk"))
                elif _level==4:logging.error(content.decode("utf-8").encode("gbk"))
                elif _level==5:logging.critical(content.decode("utf-8").encode("gbk"))
                else: pass




    def log2all(self,filename="log.log"):
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
        #
        # #################################################################################################
        # #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        # console = logging.StreamHandler()
        # console.setLevel(logging.INFO)
        # formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        # console.setFormatter(formatter)
        # logging.getLogger('').addHandler(console)
        # #################################################################################################
        #
        # logging.debug('This is debug message')
        # logging.info('This is info message')
        # logging.warning('This is warning message')


if __name__ == '__main__':
        log = LOG()
        # log.log2file(1,"log.log","大家好111")
        # log.log2file("test.log","大家好111")

        # log.log2file("打算的撒")
        # log.log2file("打算的撒",level=2)
        # log.log2file("打算的撒",level=2,filename="hello.log")
        # log.log2file_help()
        log.log2file("打算的撒",level=5,format="A",datefmt="custom",filemode="a")
        # content1 = "hello 大家好 "