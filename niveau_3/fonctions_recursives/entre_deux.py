#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def afficher(l,a,b):
    l.append(a)
    if a != b :
        afficher(l,a+1,b)


def main():
    a,b = [ int(e) for e in sys.stdin.readline().split(' ') ]
    
    l = []
     
    afficher(l,a,b)
    print(" ".join(map(str,l)))

if __name__ == '__main__':
    main()