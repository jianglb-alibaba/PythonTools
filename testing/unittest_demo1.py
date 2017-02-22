# -*- coding: utf-8 -*-

# !/usr/bin/python

# Filename: func_doc.py
# Author: jianglb-alibaba
# mail: 419331434@qq.com

import unittest
import myclass1

def sum( x, y):
        return x+y


def sub( x, y):
        return x-y


class mytest(unittest.TestCase):  
      
    ##初始化工作  
    def setUp(self):  
        print("test before")
      
    #退出清理工作  
    def tearDown(self):  
        print("test after")
      
    #具体的测试用例，一定要以test开头  
    def testsum(self):  
        # self.assertEqual(myclass1.sum(1, 2), 2, 'test sum fail')
        self.assertEqual(myclass1.sum("1", 1.0), 2)
          
          
    def testsub(self):  
        # self.assertEqual(myclass1.sub(2, 1), 1, 'test sub fail')
        self.assertEqual(myclass1.sub(2, 1), 1)

          
          
if __name__ =='__main__':  
    unittest.main()  