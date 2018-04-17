# -*- coding:utf-8 -*-

__author__ = "kiya04-16"
# 异常处理的两种方式
try:
    10/0
    print(num)
    print("----1----")
# except (NameError, ZeroDivisionError):
#     print('有异常了')
except Exception:

    print('有异常了')



print('-----2---')