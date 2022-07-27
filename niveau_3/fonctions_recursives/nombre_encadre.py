#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def encadre(l,n):
    if l.count('[') == n:
        return l
    else:
        return encadre(['['] + l + [']'],n)

def main():
    nb,n = [ int(e) for e in sys.stdin.readline().split(' ') ]
    
    print("".join(encadre([str(nb)],n)))

if __name__ == '__main__':
    main()