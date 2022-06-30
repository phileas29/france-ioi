#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    l=[]
    while True:
        try:
            l += map(int,input().split(' '))
        except:
            break
    print(sum(l))


if __name__ == '__main__':
    main()