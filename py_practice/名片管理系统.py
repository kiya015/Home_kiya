# -*- coding:utf-8 -*-
__author__ = 'kiya'

#功能：
#对字典做增、删、改、查操作

print('=' * 50)
print('名片管理系统V1.0')
print('所有功能：1、新增;2、查询;3、修改;4、删除;5、退出系统 ')
# print('请输入您要增加的信息：')
# print('请输入您要查询的信息：')
# print('请输入您要修改的信息：')
# print('请输入您要删除的信息:')
print('=' * 50)

name_list = [
	{'name':'kiya','age':28,'address':'湖南','work':'testing'}
	]
# name_list = [
	# {'name':'kiya','age':28,'address':'湖南','work':'testing'},
	# {'name':'locun','age':18,'address':'河南','work':'dev'},
	# {'name':'kiya','age':28,'address':'香港','work':'hash'}
	# ]

while True:

	function =  int(input('选择操作[1、新增;2、查询;3、修改;4、删除;5、退出系统]：'))

	#增加内容
	if function == 1:
		new_name = input('输入姓名：')
		new_age = input('输入年龄：')
		new_address = input('输入地址：')
		new_work = input('输入工作：')
		# name_list.extend(content)
		card_dict = {}
		card_dict['name'] = new_name
		card_dict['age'] = new_age
		card_dict['address'] = new_address
		card_dict['work'] = new_work

		name_list.append(card_dict)#将对应增加的字典添加至列表

		print('您添加的内容是:%s' % card_dict)
		# print('新列表数据为：%s' % name_list)
	#查询内容
	elif function == 2:
		new_name = input('输入您要查询的姓名：')
		find_flag = 0 #定义是否找到的标签
		for i in name_list:
			# print(i)
			if new_name == i['name']:
				print('您查找的%s信息：\nname：%s\nage:%s\naddress:%s\nwork:%s' % (new_name, i['name'], i['age'], i['address'], i['work']))
				find_flag = 1#表示找到了
				break  #查到后结束循环
		if find_flag == 0:#循环结束后没有查到此信息
			print('查无此人！')
	#修改某项内容，如姓名
	elif function == 3:
		new_name = input('您要修改的姓名：')
		find_flag = 0
		for i in name_list:
			# print(i)
			if new_name == i['name']:
				print(i['name'])
				choice_name = input('将%s修改为:' % new_name)
				i['name'] = choice_name
				print('已将%s修改为：%s\n列表为%s' % (new_name, choice_name, i))
				find_flag = 1
				break
		# print('')
		# print(name_list)
		if find_flag == 0:
			print('查无此项')
	# 删除某个内容，如姓名
	elif function == 4:
		new_name = input('输入您要删除的姓名：')
		find_flag = 0
		for i in name_list:
			if new_name == i['name']:
				del i['name']
				print(name_list)
				find_flag = 1
				break
		if find_flag == 0:
			print('查不到此人，无法删除')
	elif  function == 6:
		print(name_list)
	elif function == 5:
		print('退出系统！')
		break
	else:
		print('输入有误，请重试哟')


