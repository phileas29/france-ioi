#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n,p = [ int(e) for e in sys.stdin.readline().split(' ') ]
    
    studentsAbsent = [True]*(p+1)
    firstAbsent = 1
    for i in range(p):
        x = int(sys.stdin.readline())
        if x-1 < p+1:
            studentsAbsent[x-1] = False
        if p == n and i == p-1:
            print(-1)
        else:
            while not studentsAbsent[firstAbsent-1]:
                firstAbsent += 1
            print(firstAbsent)

if __name__ == '__main__':
    main()