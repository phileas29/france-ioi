#!/bin/python3
# -*- coding: utf-8 -*-

def conv(s):
    try:
        return int(s)
    except:
        return s

def build(dim,elts):
    map = [ [ '.' for j in range(dim[1]) ] for i in range(dim[0]) ]
    for i in range(dim[0]):
        for j in range(dim[1]):
            for elt in elts:
                if elt[0] <= i and i <= elt[2] and \
                    elt[1] <= j and j <= elt[3] :
                    map[i][j] = elt[-1]
    return map

def show(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j],end='')
        print()

def main():
    dim = list(map(int,input().split(' ')))
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(conv,input().split(' '))))
    show(build(dim,l))

if __name__ == '__main__':
    main()