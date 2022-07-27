#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    tab = [ int(e) for e in input().split(' ')[:n] ]
    swap = []
    tmp = 0

    for i in range(1,n+1):
        indexCurrent = tab.index(i)
        for j in range(max(0,indexCurrent-(i-1))):
            swap.append([tab[indexCurrent-j-1],tab[indexCurrent-j]])
            tab[indexCurrent-j-1],tab[indexCurrent-j] = tab[indexCurrent-j],tab[indexCurrent-j-1]

    print(len(swap))
    for l in swap:
        print(" ".join(map(str,l)))

if __name__ == '__main__':
    main()