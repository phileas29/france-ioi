#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    
    stack = []
    x = 0
    for _ in range(n):
        s = sys.stdin.readline().strip()
        if s[0] == 'C':
            x = int(s.split(' ')[-1])
            while len(stack) != 0 and stack[-1] <= x :
                stack.pop()
            stack.append(x)
        else:
            print(len(stack))

if __name__ == '__main__':
    main()