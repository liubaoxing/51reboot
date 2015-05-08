#!/bin/env python
user = ['zhao','qian','sun']
passwd = ['123','456','789']
goods = ['apple','banana','orange']
packet = []
num = [0] * len(user)

while True:
    u = raw_input('login user: ')
    p = raw_input('password: ')
    if u not in user or  not u or not p:
        print 'invalid user or password,input again'
        continue
    elif num[user.index(u)] == 3:
        print 'this user has failed 3 times'
        continue
    else:
        if p == passwd[user.index(u)]:
            num[user.index(u)] = 0
            print 'welcom %s,please buy something: %s' % (u,goods)
            while True:
                g = raw_input('input: ')
                if not g:
                    print 'nothing add to packet: %s' % packet
                elif g == 'exit':
                    print 'xxxxxxxxxxxxxxxxxx'
                    break
                elif g not in goods:
                    print "we don't have this goods: %s" % packet
                    continue
                elif g in packet:
                    print 'you have buy this goods: %s' % packet
                    continue
                else:
                    packet.append(g)
                    print 'add to your packet successfully: %s' % packet
        else:
            print 'password faild'
            num[user.index(u)] += 1
