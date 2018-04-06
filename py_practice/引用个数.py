# -*- coding:utf-8 -*-

__author__ = 'kiya04-6'

# 测量对象的引用个数
import sys

class T:
    pass


t = T()

print(sys.getrefcount(t))