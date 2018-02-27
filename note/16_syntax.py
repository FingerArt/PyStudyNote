# coding=utf-8

# if
if 3 < 2:
    print 'ok'
else:
    print 'no'

if 4 > 5:
    print 'ok'
elif 4 < 5:
    print 'no'

# while

counter = 0
while counter < 3:
    print 'loop #%d' % counter
    counter += 1

# for

for item in ['orange', 'apple', 'banana', 'grape']:
    print item,

print

for item in range(3):
    print item

str = 'hello world!'
for item in range(len(str)):
    print str[item], '(%d)' % item

# 将for写在一行
print [x ** 2 for x in range(4)]
print [x ** 2 for x in range(4) if not x % 2]

