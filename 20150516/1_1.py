#!/bin/env python
logfile = "/home/liubx/51reboot/www_access_20140823.log"
result_dic = {}
result = []
try:
    f = open(logfile)
    while True:
        content = f.readline()
        if content:
            tem_l = content.strip().split(' ')
            result_dic[(tem_l[8],tem_l[6],tem_l[0])] = result_dic.get((tem_l[8],tem_l[6],tem_l[0]),0) + 1
        else:
            f.close()
            break
    for i in sorted(result_dic.items(),key=lambda arr:arr[1])[:-10:-1]:
        print i
except IOError,e:
    print e
