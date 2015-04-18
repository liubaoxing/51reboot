mylist = [65555,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for a in range(len(mylist)):
    for b in range(a+1,len(mylist)):
        if mylist[b] < mylist[a]:
            temp = mylist[a]
            mylist[a] = mylist[b]
            mylist[b] = temp
        print mylist
