# -*- coding: utf-8 -*-

# !/usr/bin/python

# Filename: func_doc.py
# Author: jianglb-alibaba
# mail: 419331434@qq.com


class myclass():
    def multiply(a, b):
        return a * b

    def sum(self,x, y):
        return x + y

    def sub(self,x, y):
        return x - y

    def list_sort(self,mylist):
        if isinstance(mylist,list):
            result = sorted(mylist, reverse=True)  #reverse=True从大到小排序
        else:
            print("it is not a list type")
            return
        return result

    def dict_sort(self,mydict):
        if isinstance(mydict,dict):
            result = sorted(mydict, reverse=True) #reverse=True从大到小排序
        else:
            print("it is not a dict type")
            return
        return result


if __name__ == '__main__':
    my = myclass()
    aa =[12,33,0.1,32,99]
    print(my.list_sort(aa))