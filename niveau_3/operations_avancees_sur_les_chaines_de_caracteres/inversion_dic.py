#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    l=[]
    n=int(input())
    for _ in range(n):
        l.append(input().split(' '))
    l.sort(key=lambda x: x[1])
    for i in range(len(l)):
        print(l[i][1]+' '+l[i][0])

if __name__ == '__main__':
    main()