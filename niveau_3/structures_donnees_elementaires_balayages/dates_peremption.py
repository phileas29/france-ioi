#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    stack = []
    
    for _ in range(n):
        transaction = [ int(e) for e in sys.stdin.readline().split(' ')[:2] ]
        if transaction[1] == 0 :
            while transaction[0] != 0:
                stack[-1][0] -= 1
                transaction[0] += 1
                if stack[-1][0] == 0:
                    stack.pop()
        else:
            if len(stack) == 0 or stack[-1][1] != transaction[1]:
                stack.append(transaction)
            else:
                stack[-1][0] += transaction[0]

    sys.stdout.write(str(min(stack,key=lambda x:x[1])[-1]))

if __name__ == '__main__':
    main()