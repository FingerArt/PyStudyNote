try:
    filename = raw_input('Enter file name: ')
    file = open(filename)
    for line in file:
        print line,
    file.close()
except IOError, e:
    print 'file open error:', e