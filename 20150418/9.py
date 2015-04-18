oldlist = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
newlist = []
for i in oldlist:
    if i not in newlist:
        newlist.append(i)
print newlist
