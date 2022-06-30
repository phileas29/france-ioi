#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    res = []
    for k in range(n):
        s = input().lower()
        for i in range(len(s)):
            if s[i] not in "abcdefghijklmnopqrstuvwxyz_" and ( i == 0 or s[i] not in "0123456789" ) :
                res.append('NO')
                break
        if len(res) == k :
            res.append('YES')
    for r in res:
        print(r)
        
if __name__ == '__main__':
    main()