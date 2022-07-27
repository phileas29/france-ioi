#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def sierpinski(drawing,n,origin):
    for k in range(n):
        drawing[origin[0]+k][origin[1]+n-1-k] = '#'
        drawing[origin[0]+k][origin[1]+0    ] = '#'
        drawing[origin[0]+0][origin[1]+k    ] = '#'
    if n != 1:
        sierpinski(drawing,n//2,[origin[0]+0   ,origin[1]+0   ])
        sierpinski(drawing,n//2,[origin[0]+n//2,origin[1]+0   ])
        sierpinski(drawing,n//2,[origin[0]+0   ,origin[1]+n//2])

def main():
    n = int(sys.stdin.readline())

    drawing = [ [ ' ' for _ in range(n) ] for __ in range(n) ]
    
    sierpinski(drawing,n,[0,0])
    for l in drawing:
        print("".join(l))

if __name__ == '__main__':
    main()