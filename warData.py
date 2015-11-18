__author__ = 'yaelcohen'




f = open('/Users/yaelcohen/Downloads/167663_ucdp.prio.armed.conflict.v4.2013 2/ucdp.csv', 'rw')
text = f.read()
lines = str.split(text, '\n')
index = 1
while index < len(lines):
    parts = str.split(lines[index], ',')
    index += 1
    print parts[0], parts[1]
print 'Done!'
print index