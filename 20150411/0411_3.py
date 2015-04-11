num_total = 0
init_status = 1
while init_status:
    num = raw_input('input num: ')
    if num == 'pc':
        init_status = 0
    else:
        num_total += int(num)
print num_total
