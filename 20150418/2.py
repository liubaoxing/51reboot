demo_list = [-2,1,65555,255,3,2,12,3,1,3,21]
max_v = demo_list[0]
min_v = demo_list[0]
num = 0
for i in demo_list:
    if i > max_v:
        max_v = i
    if i < min_v:
        min_v = i
    num += 1
print max_v,min_v,num
