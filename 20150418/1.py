demo_list=[1,2,'a','b',[4,5,6]]
a = 1
for i in demo_list:
    if a == i:
        print '%s is in demo_list' % a
        break
    print '%s is not in demo_list' % a
