# coding=utf-8
# 输出
import sys

print 'hello world!'

print 'hello', 'world', '!'  # 这种方式会用一个空格将各部分拼起来

print '你好世界',# 通过加上逗号(,)避免换行

print 'hello %d%s' % (9, '!')  # 两个%代表%


print >> sys.stderr, 'output error.'  # 将输出重定向到标准错误
