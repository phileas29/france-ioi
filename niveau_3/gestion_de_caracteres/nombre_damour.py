#!/bin/python3
# -*- coding: utf-8 -*-

def res(e):
    s = sum(e)
    while 9 < s :
        s = sum(map(int,str(s)))

    return s

def rect(e):
    return ord(e)-65

def main():
    d = input().split(' ')
    s1 = res(map(rect,d[0]))
    s2 = res(map(rect,d[1]))
    print("{} {}".format(s1,s2))

if __name__ == '__main__':
    main()