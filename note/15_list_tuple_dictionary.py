# coding=utf-8

# 列表[]
# 元素的个数及元素的值可以改变
list = [0, 1, 2, 3, 4]

print list[3]
print list[2:4]

list.append('add')
list[2] = '2'
list.insert(0, 'insert')

print list

# 元组()
# 元素不可以更改（尽管他们的内容可以），元组可以看成是只读的列表
tuple = (0, 1, 2, 3, 4)

print tuple[3]
print tuple[2:4]

# 字典
# 映射数据类型

login = {'host': 'chengguo.io'}
login['port'] = 80

for key in login:
    print key, login[key]