#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    p = [ int(e) for e in input().split(' ') ]
    pp = [ int(e) for e in input().split(' ') ]
    pp.sort(reverse=True)
    out = []
    for e in pp[:p[1]]:
        out.append(e)
    print(" ".join(map(str,out)))

if __name__ == '__main__':
    main()