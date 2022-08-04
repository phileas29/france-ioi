#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    N, n = [ int(e) for e in sys.stdin.readline().split(' ') ]
    Ni = [ int(e) for e in sys.stdin.readline().split(' ') ]
    
    print(sum([ Ni[i] * N ** (n-1-i) for i in range(n) ]))

if __name__ == '__main__':
    main()