#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    tab = [ [ int(e) for e in input().split(' ')[:2] ] for _ in range(n) ]
        
    tab.sort(key=lambda row: (row[1],row[0]))

    for r in tab:
        print(*r)

if __name__ == '__main__':
    main()