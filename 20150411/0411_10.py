mylist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
first = mylist[0]
second = mylist[0]
for element in mylist:
    if element > first:
        second = first
        first = element
print 'the max num %s,the second num %s' % (first,second)
