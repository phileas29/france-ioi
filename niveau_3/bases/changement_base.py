#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    Bin,Bout,Nin = [ int(e) for e in sys.stdin.readline().split(' ') ]
    x = [ int(e) for e in sys.stdin.readline().split(' ') ][::-1]
    y = sum([ x[i] * Bin ** i for i in range(Nin) ])

    z = []
    while True:
        z.append(y%Bout)
        y = ( y - z[-1] ) // Bout
        if y == 0:
            break
            
    print(" ".join([ str(e) for e in z ][::-1]))

if __name__ == '__main__':
    main()