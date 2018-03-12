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
# f_write = open(new_file_name,'w')  # 打开新文件

# 将源文件内容写入新的new_file.txt中
# new_file = f_write.write(f_read)
# f_write.close()  # close新文件
# newread = open('new_file.txt','r')  #  打开新文件
# print (newread.read())   # 打印新文件内容
# newread.close()   # 关闭新文件
# f_open.close()    # 关闭源文件
# # print(f_write.read())


# 文件的定位读写

# f_file = open('test.txt','r')
# f_file.close()
# print(f_file.seek(2,0)) # seek()  2往右偏移，-2住左偏移；0,文件开始，1当前位置，2文件结尾
# print(f_file.read())

# 文件读取的其它方式 readlines\readline
#
# f = open('new_file.txt')
# # a = f.readline()
# b = f.readlines()
# # print(a)
# print(b)


# 大文件分步读取实现
f = open('工时计算实操.py', 'rb')
# f = open('工时计算实操.py','r', encoding='utf8')
f_old = f.read()
# print(f_old)
new = open('newa.txt', 'wb+')
f_new = new.write(f_old)  # 写入完成后光标移到了最后一位

new.seek(0, 0)  # 将光标移到文档开始位置
print(new.read())



# 打开半读取原文件
# f = open('工时计算实操.py','rb')
# a = f.read()
# print(a)
# 创建并写入新文件
# f_new = open('new_file.txt', 'w' ,coding = 'utf-8')  # 创建新文件为new_file.txt
# f_new = open('new_file.txt', 'wb+')  # 创建新文件为new_file.txt 'wb+' 表示可写且读,b表示二进制方式
# file = f_new.write(a)  # 将读出来的f文件字节a写入新创建的文件中
# f_new.seek(0,0) #  写入时光标移入结尾，此操作将光标移到开始处
# print(f_new.read())   #  对应'wb+'模式
# f_new.close()  # 对应'wb'模式
# b = open('new_file.txt', 'rb')
# print(b.read())


# 对大文件进行复制----实现方式：通过部分读写的方式去实现
# 先创建一个新的文件
f_new = open('new_file0305.txt', 'w' ,encoding = 'utf-8')
# 打开原文件进行读且写入新文件中
f = open('工时计算实操.py','r', encoding = 'UTF-8')
while True:
    a = f.read(1024)
    # print(type(a))
    if len(a) == 0:  # 当字节写入长度为0时，说明写入完毕，即跳出循环
        break
    b = f_new.write(a)
f.seek(0,2)
print(len(f.read(1)))  # 验证if len(a) == 0原理



