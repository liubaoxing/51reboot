#!/bin/env python
def operate(input_str):
    tmp_l = list(input_str)
    for i in range(len(tmp_l)):
        if tmp_l[i] == '+' or tmp_l[i] == '-' or tmp_l[i] == '*' or tmp_l[i] == '/':
            tmp_l[i] = '_' + tmp_l[i] + '_'
    math_l = ''.join(tmp_l).split('_')
    while True:
        if '*' in math_l:
            math_l[math_l.index('*')-1:math_l.index('*')+2] = [float(math_l[math_l.index('*')-1]) * float(math_l[math_l.index('*')+1])]
        elif '/' in math_l:
            math_l[math_l.index('/')-1:math_l.index('/')+2] = [float(math_l[math_l.index('/')-1]) / float(math_l[math_l.index('/')+1])]
        elif '+' in math_l:
            math_l[math_l.index('+')-1:math_l.index('+')+2] = [float(math_l[math_l.index('+')-1]) + float(math_l[math_l.index('+')+1])] 
        elif '-' in math_l:
            math_l[math_l.index('-')-1:math_l.index('-')+2] = [float(math_l[math_l.index('-')-1]) - float(math_l[math_l.index('-')+1])]
        else:
            return math_l[0]
while True:
    content = raw_input('input a math expression: ')
    if content:
        print 'the value of your input num: %f' % operate(content)
    else:
        continue
