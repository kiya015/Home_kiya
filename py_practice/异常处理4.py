#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 22:49
# @Author  : kiya
# @Site    : 
# @File    : 异常处理4.py
# @Software: PyCharm

# 异常中抛出异常
class Test(object):
    def __init__(self, switch):
        self.switch = switch

    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print('捕捉到异常')
                print(result)
        else:
            raise

a = Test(True)
a.calc(10, 0)

print('============================')

a.switch = False
a.calc(10, 0)