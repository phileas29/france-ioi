#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    n = int(sys.stdin.readline())
    tab = [ [ None for j in range(n-i) ] for i in range(n) ]

    for i in range(n):
        for j in range(n):
            if i<=j:
                tab[i][j-i]=bin((1+i)*(1+j))[2:]
                sys.stdout.write(tab[i][j-i])
            else:
                sys.stdout.write(tab[j][i-j])
            sys.stdout.write("\t")
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()