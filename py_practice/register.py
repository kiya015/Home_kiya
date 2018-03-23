# -*- coding:utf-8 -*-

__author__ = 'kiya3-22'

import requests
import redis
import time

# 注册接口地址



# 手机号
phone = 13600175152
# print(type(phone))
code = 123452
pwd = 'qweqwe'
# 无法跳过图片验证码，但可以直接往redis插入数据实现注册流程

# 连接redis


r = redis.Redis(connection_pool=pool)



d = requests.post(url, postData)
print(d.content)

print(d.json().get('message'))




