#!/bin/python3
# -*- coding: utf-8 -*-

def whatSqr(X,n):
    x,y = X
    h,k = n-1,n-1
    return (abs((x-h)+(y-k))+abs((x-h)-(y-k)))//2

if __name__ == '__main__':
    nbSqr = int(input())
    n = nbSqr*2-1

    for i in range(n):
        for j in range(n):
            print(chr(97+(nbSqr-1)-whatSqr([j,i],nbSqr)),end='')
        print()

    exit()
