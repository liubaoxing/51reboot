mylist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
newlist = []
for i in mylist:
    if len(newlist) == 0 or i > newlist[len(newlist)-1]:
        newlist.append(i)
    else:
        for n in range(len(newlist)):
            if i <= newlist[n]:
                newlist.insert(n,i)
                break
#    print newlist
print newlist
