l = [(1,4),(5,1),(2,3)]
print sorted(l,key=lambda x:max(x))
print sorted(l,key=lambda (x,y): x * (x > y) + y * (x <= y))
