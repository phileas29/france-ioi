#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def toto(s,n):
    if n == 0:
        return s
    else:
        return toto(s,n-1).replace("0","(0 + 0)")

def main():
    n = int(sys.stdin.readline())
    
    print("0 = "+toto("0",n))

if __name__ == '__main__':
    main()