#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    n = [ int(e) for e in sys.stdin.readline().strip() ]
    
    print(sum([ b*2**i for i,b in enumerate(n[::-1]) ]))

if __name__ == '__main__':
    main()