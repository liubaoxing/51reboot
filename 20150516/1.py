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
    def func_sort(arr):
        return arr[1]
    for i in sorted(result_dic.items(),key=func_sort)[-10:]:
        print i
#    for k,v in result_dic.items():
#       result.append([k[0],k[1],(k[2],result_dic[k])])
#    for i in range(10):
#        for n in range(len(result)-i-1):
#            if result[n+1][2][1] < result[n][2][1]:
#                result[n],result[n+1] = result[n+1],result[n]
#        print result[-1 - i]
except IOError,e:
    print e
