# -*- coding:utf-8 -*-

__author__ = 'kiya3-22'

import http
import redis

# 注册接口地址

url = 'http://testeps.rabbitpre.com/api/user/loginqrcode'

# 无法跳过图片验证码，但可以直接往redis插入数据实现注册流程

# 连接redis

pool = redis.ConnectionPool(host = '172.16.1.1',port = '443')

r = redis.Redis(connection_pool=pool)




