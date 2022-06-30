#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    s = input().upper()
    maxi = ['',0]
    alpha = {chr(65+c):0 for c in range(26)}
    for c in s:
        if c != ' ' :
            alpha[c] += 1
            if maxi[1] < alpha[c] :
                maxi[0] = c
                maxi[1] = alpha[c]
    print(maxi[0])

if __name__ == '__main__':
    main()