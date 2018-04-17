#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 23:10
# @Author  : kiya
# @Site    : 
# @File    : 异常处理2.py
# @Software: PyCharm

import time

try:
    f = open('new_file0305.txt', 'rb')  # 方法一：打开文件两种解决编码问题的方法
    try:
        while True:
            count = f.readlines()
            if len(count) == 0:
                break
            time.sleep(2)
            print(count)
    except Exception as ret:
       pass
        # print('为空文件')
    finally:
        f.close()
        print('关闭文件')
except Exception:
    print('文件不存在')


a = open('new_file0305.txt', encoding = 'utf-8')  # 方法二：打开文件两种解决编码问题的方法
# # print(type(a))
b = a.read()
print(b)