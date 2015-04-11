num_total = 0
count = 0
while True:
    num = raw_input('input num: ')
    if not num:
        break
    else:
        count += 1.0
        num_total += int(num)
print num_total / count
