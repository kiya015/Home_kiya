#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 23:25
# @Author  : kiya
# @Site    : 
# @File    : 异常处理3.py
# @Software: PyCharm

class ShortInputException(Exception):
    def __init__(self,length, atleast):
        self.length = length
        self.atleast = atleast




def main():
    try:
        s = input("请输入")
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:
        print('ShortInputException:输出长度是%d,长度至少是：%d'% (result.length, result.atleast))
    else:
        print('无异常')

main()