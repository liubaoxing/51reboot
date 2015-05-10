#!/bin/env python
wd_l = []
wd_sum = 0

f = open('/tmp/tem.txt')
content = f.read().strip().split('\n')
f.close()

for i in content:
    wd_l.append(float(i.split(' ')[1]))
    wd_sum += float(i.split(' ')[1])
print 'avg: %s,max: %s' % (wd_sum / len(wd_l),max(wd_l))
