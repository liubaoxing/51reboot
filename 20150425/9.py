content = raw_input('input: ')
content.replace(r';',r':')
d = {}
for i in content.split(','):
    d[i.split(':')[0]] = i.split(':')[1]
print d
