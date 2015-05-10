#!/bin/env python
logfile = "/home/liubx/51reboot/www_access_20140823.log"
resultfile = "/tmp/result.txt"
result_l = []
result = []
try:
    f = open(logfile)
    while True:
        content = f.readline()
        if content:
            tem_l = content.strip().split(' ')
            result_l.append([tem_l[8],tem_l[6],tem_l[0]])
        else:
            f.close()
            break
    for i in result_l:
        count = result_l.count(i)
        new_element = [i[0],i[1],(i[2],count)]
        if new_element not in result:
            if len(result) == 0 or count <= result[-1][2][1]:
                result.append(new_element)
            else:
                for num in range(len(result)):
                    if count >= result[num][2][1]:
                        result.insert(num,new_element)
                        break
    if result:
        r = open(resultfile,'w')
        for i in result:
            r.write(str(i)+'\n')
        r.close()
except IOError,e:
    print e
