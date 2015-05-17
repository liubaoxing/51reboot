#!/bin/env python
def operate(input_str):
    math_l = list(input_str)
    while True:
        if ' ' in math_l:
            math_l.remove(' ')
        elif '*' in math_l:
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
        print 'the sum of your input num: %f' % operate(content)
    else:
        continue
