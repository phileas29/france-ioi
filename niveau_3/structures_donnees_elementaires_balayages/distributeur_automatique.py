#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    queue = []
    
    for _ in range(n):
        transaction = [ int(e) for e in sys.stdin.readline().split(' ')[:2] ]
        if transaction[1] == 0 :
            while transaction[0] != 0:
                queue[0][0] -= 1
                transaction[0] += 1
                if queue[0][0] == 0:
                    queue.pop(0)
        else:
            if len(queue) == 0 or queue[-1][1] != transaction[1]:
                queue.append(transaction)
            else:
                queue[-1][0] += transaction[0]

    sys.stdout.write(str(min(queue,key=lambda x:x[1])[-1]))

if __name__ == '__main__':
    main()