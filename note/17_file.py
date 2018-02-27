handle = open('17_file.py', 'r')
print handle.readline(),

for line in handle:
    print line,

handle.close()