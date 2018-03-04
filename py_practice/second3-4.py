# -*- coding:utf-8 -*-

__author__ = 'kiya3-4'

# 斐波那契数列
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……

# 方法一
# def Fib(n):
#     a, b = 0, 1
#     while n:
#         a, b, n = b, a + b, n - 1
#         print(a)
# Fib(1)

# 文件读写操作

# f = open("test.txt",'w')
# f.write('test file rw ')
# f.close()

# b = open("F:\Home_kiya\Py_everyday_practice\\test.txt","r")
# print(b.read())
# b.close()

# 文件备份

# old_file = input('请输入要复制的文件（txt）：')
# f_open = open(old_file,'r')  # 打开原文件
# f_read = f_open.read()  # 读取源文件
# # f_write = open('new_file.txt','w')  # 创建新文件名(自建新文件名)
# position = old_file.find('.')  # 通过切分test.txt在.前面加上[复制]
# print(position)  # find()找到.的位置
#
# # 通过.将文件名进行切分
# new_file_name = old_file[:position] + '[复件]' + old_file[position:]
# print(new_file_name)
# f_write = open(new_file_name,'w')
#
# new_file = f_write.write(f_read)   # 将源文件内容写入新的new_file.txt中
# f_write.close()  # close新文件
# newread = open('new_file.txt','r')  #  打开新文件
# print (newread.read())   # 打印新文件内容
# newread.close()   # 关闭新文件
# f_open.close()    # 关闭源文件
# # print(f_write.read())


# 文件的定位读写

f_file = open('test.txt','r')
# f_file.close()
print(f_file.seek(2,0)) # seek()  2往右偏移，-2住左偏移；0,文件开始，1当前位置，2文件结尾
print(f_file.read())
