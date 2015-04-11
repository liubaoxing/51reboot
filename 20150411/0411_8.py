while True:
    year = raw_input('input the year: ')
    if not year:
        print 'bye'
        break
    elif int(year) % 100 == 0:
        if int(year) % 400 == 0:
            print '%s is runnian' % year
        else:
            print '%s is not runnian' % year
    elif int(year) % 4 == 0:
        print '%s is runnian' % year
    else:
        print '%s is not runnian' % year
