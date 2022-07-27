#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def hanoi(l,n,s,i,e):
    if n != 0:
        hanoi(l,n-1,s,e,i)
        l[e].append(l[s].pop())
        print(str(s+1)+" -> "+str(e+1))
        hanoi(l,n-1,i,s,e)

def main():
    n = int(sys.stdin.readline())
    l = [[ n-j for j in range(n) ],[],[]]
    hanoi(l,n,0,1,2)

if __name__ == '__main__':
    main()