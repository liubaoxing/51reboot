d = {'k1':'v1','k2':'v2','k3':'v3'}
d1 = {'k1':'v4','k4':'v4'}
for i in d1:
    d[i] = d1[i]
print d
