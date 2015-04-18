mylist = [1,2,3,4,2,12,3,1,4,3,21,2,2,3,4111,22,3333,4]
n = mylist.index(4)
num = n
for v in mylist[n+1:]:
    num += 1
    if v == 4:
        break
print num
