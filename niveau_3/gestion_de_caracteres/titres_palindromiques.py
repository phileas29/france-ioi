#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    l = []
    ll = []
    for _ in range(n):
        l.append(input())
        ll.append(l[-1].upper().replace(' ',''))
    res = [ True for _ in range(len(l)) ]
    for k,s in enumerate(ll):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                res[k] = False
                break

    for k,s in enumerate(l):
        if res[k] :
            print(s)
        
if __name__ == '__main__':
    main()