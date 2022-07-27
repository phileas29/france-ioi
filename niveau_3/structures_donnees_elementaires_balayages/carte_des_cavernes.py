#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    dic = {'(':1,')':-1}
    n = int(sys.stdin.readline())
    tree = list(sys.stdin.readline().replace(' ','').strip())

    n = len(tree)
    integral = 0
    i = 0
    while i < n and -1 < integral :
        integral += dic[tree[i]]
        i += 1
    
    if integral == 0:
        print(1)
    else:
        print(0)

    # function = [ dic[c] for c in tree ]
    # integral = [ sum(function[:i+1]) for i in range(len(function)) ]

    # if min(integral) < 0 or integral[-1] != 0 :
    #     sys.stdout.write('0')
    # else:
    #     sys.stdout.write('1')

if __name__ == '__main__':
    main()