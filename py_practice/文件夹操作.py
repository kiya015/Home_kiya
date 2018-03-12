# -*- coding:utf-8 -*-


__author__ = 'kiya3-10'

# 文件批量重命名
# 1.输入需要命名的文件
# 2.获取文件夹中所有的文件名
# 3.找到要重命名的文件

import os


f_name = input('您要重命名的文件是：')

# f_list = os.listdir(r'F:\Home_kiya\py_practice')
f_list = os.listdir(r'F:\Home_kiya\py_practice')

# print(f_list)
# os.chdir()  # 进入某目录

for i in f_list:
    # print(i)
    if i == f_name:
        new_name = os.rename(f_name,('修改' + f_name))
        print(f_name)

