#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def findByDicho(tab,elt):
    n = len(tab)
    inf = 0
    sup = n-1
    while True:
        middle = ( inf + sup ) // 2
        if tab[middle] == elt :
            return tab[middle]
        else:
            if sup <= inf :
                tab2 = [ abs(elt-tab[(middle+i)%n]) for i in range(-1,2) ]
                return tab[(middle+tab2.index(min(tab2))-1)%n]
            if elt < tab[middle] :
                sup = middle - 1
            elif tab[middle] < elt:
                inf = middle + 1

def main():
    n = int(sys.stdin.readline())
    densities = [ int(e) for e in sys.stdin.readline().split(' ')[:n] ]
    q = int(sys.stdin.readline())
    requests = [ int(sys.stdin.readline()) for _ in range(q) ]

    densities.sort()
    results = []

    for req in requests:
        print(findByDicho(densities,req))

if __name__ == '__main__':
    main()