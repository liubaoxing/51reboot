mylist = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
count = {}
for element in mylist:
    if element in count:
        count[element] += 1
    else:
        count[element] = 1
for e in count:
    print e,count[e]
