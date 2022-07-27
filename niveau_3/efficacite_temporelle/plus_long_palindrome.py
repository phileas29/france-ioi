#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    maxPalindromeLength = 1
    s = sys.stdin.readline()
    n = len(s)

    for j in [ n//2 + (((i+1)%2)*2-1)*((i+1)//2) for i in range(n)]:
        for i in range(min(j,n-j-1)+1):#odd
            if s[j-i] != s[j+i]:
                break
            elif maxPalindromeLength < 1+2*i :
                maxPalindromeLength = 1+2*i

        for i in range(min(j,n-j-2)+1):#even
            if s[j-i] != s[j+i+1]:
                break
            elif maxPalindromeLength < 1+2*i+1 :
                maxPalindromeLength = 1+2*i+1

    print(maxPalindromeLength)

if __name__ == '__main__':
    main()