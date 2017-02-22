# -*- coding: utf-8 -*-

# !/usr/bin/python

# Filename: func_doc.py
# Author: jianglb-alibaba
# mail: 419331434@qq.com

import unittest
import myclass
class mytest(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        self.tclass = myclass.myclass()   ##实例化了被测试模块中的类

    # 退出清理工作
    def tearDown(self):
        pass

    # 具体的测试用例，一定要以test开头
    def testsum(self):
        self.assertEqual(self.tclass.sum(1, 2), 2, 'test sum fail')

    def testsub(self):
        self.assertEqual(self.tclass.sub(2, 1), 1, 'test sub fail')


if __name__ == '__main__':
    unittest.main()
