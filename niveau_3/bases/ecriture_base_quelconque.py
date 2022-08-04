#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    a, N = [ int(e) for e in sys.stdin.readline().split(' ') ]
    if a == 0:
        print("1")
        print("0")
    else:
        n = int(math.log(a,N))+1
        r = a
        d = N ** (n-1)
        Ni = []
        for i in range(n-1,-1,-1):
            Ni.append( r // d )
            r -= Ni[-1] * d
            d //= N
        
        print(n)
        print(" ".join([ str(e) for e in Ni ]))

if __name__ == '__main__':
    main()