#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    k,n = [ int(e) for e in sys.stdin.readline().split(' ') ]
    currents = [ int(current) for current in sys.stdin.readline().split(' ')[:n] ]
    
    sumCurrents = 0
    maxDeliverable = 0
    for i in range(len(currents)):
        sumCurrents += currents[i]
        if k-1 <= i:
            if i != k-1:
                sumCurrents -= currents[i-k]
            if maxDeliverable < sumCurrents:
                maxDeliverable = sumCurrents

    print(maxDeliverable)

if __name__ == '__main__':
    main()