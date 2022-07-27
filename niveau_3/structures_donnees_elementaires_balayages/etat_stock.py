#!/bin/python3
# -*- coding: utf-8 -*-

import sys

# def main():
#     n = int(sys.stdin.readline())
#     populations = [ int(e) for e in sys.stdin.readline().split(' ')[:n] ]
#     q = int(sys.stdin.readline())
#     transactions = [ [ int(e) for e in sys.stdin.readline().split(' ')[:2] ] for _ in range(q) ]
    
#     for transaction in transactions:
#         populations[transaction[0]-1] += transaction[1]

#     sys.stdout.write(" ".join(map(str,populations)))

def main():
    n = int(sys.stdin.readline())
    populations = [ int(e) for e in sys.stdin.readline().split(' ')[:n] ]
    
    for _ in range(int(sys.stdin.readline())):
        transaction = [ int(e) for e in sys.stdin.readline().split(' ')[:2] ]
        populations[transaction[0]-1] += transaction[1]

    sys.stdout.write(" ".join(map(str,populations)))

if __name__ == '__main__':
    main()