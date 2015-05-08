d = {'a':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
n = {}
for i in d:
    if d[i] not in n:
        n[d[i]] = i
    elif type(n[d[i]]) != type([]):
        n[d[i]] = [n[d[i]],i]
    else:
        n[d[i]].append(i)
print n
