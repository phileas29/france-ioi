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
            return "1\n"
        else:
            if sup <= inf :
                return "0\n"
            if elt < tab[middle] :
                sup = middle - 1
            elif tab[middle] < elt:
                inf = middle + 1
def main():
    n = int(sys.stdin.readline())
    densities = [ int(e) for e in sys.stdin.readline().split(' ')[:n] ]
    densities.sort()
    for _ in range(int(sys.stdin.readline())):
        sys.stdout.write(findByDicho(densities,int(sys.stdin.readline())))
if __name__ == '__main__':
    main()