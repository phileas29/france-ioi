#!/bin/python3
# -*- coding: utf-8 -*-

def diff(sig):
    maxi = 0.
    for i in range(len(sig)-1):
        test = abs(sig[i]-sig[i+1])
        if maxi < test:
            maxi = test

    return maxi

def lissage(inS):
    outS = [inS[0]]

    for i in range(1,len(inS)-1):
        outS.append((inS[i-1]+inS[i+1])/2)
    outS.append(inS[-1])

    return outS

if __name__ == '__main__':
    n = int(input())
    diffMax = float(input())
    out = []
    for _ in range(n):
        out.append(float(input()))

    i = 0
    sig = out
    while True:
        if diff(sig) < diffMax :
            break
        i += 1
        sig = lissage(sig)
    
    print(i)
