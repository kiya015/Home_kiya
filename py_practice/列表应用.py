# -*- conding : utf -8 -*-

__author__ = 'kiya'

#姓名管理系统

#功能：
print('=' * 50)
print('姓名管理系统V1.0')
print('1、新增一个姓名')
print('2、删除一个姓名')
print('3、修改一个姓名')
print('4、查询一个姓名')
print('=' * 50)


name = ['aaa','bbbb']
while True:
    application = int(input('输入你要操作的功能：'))
    print('=' * 50)
    print(name)
    if application == 1 :
        a = str(input('您输入您要增加的姓名：'))
        name.append(a)
        print('您增加的姓名是：%s' % a)
    elif application == 2:
        b = str(input('输入您要删除姓名：'))
        if b in name:
            name.remove(b)
            print('您删除的姓名是：%s' % b)
        else:
            print('没有这个姓名')
    elif application == 3:
        c = str(input('输入您要修改的姓名:'))
        choice = str(input('修改姓名为：'))
        if c in name:
            num = name.index(c)
            print(num)
            name[num] = choice
            print('修改 %s 为 %s 成功' % (c,choice))
        else:
            print('没有找到您要修改的姓名!')
    elif application == 4:
        d = str(input('输入您要查询的姓名：'))
        if d in name:
            print('找到了您要查询的:%s' % d)
        else:
            print('查无此人')
    elif application == 5:
        print('退出系统')
        break
    else:
        print('您输入的功能不存在')
# print(name)




