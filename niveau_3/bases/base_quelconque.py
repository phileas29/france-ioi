#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    n = int(sys.stdin.readline())

    if n== 0:
        print(0)
    else:
        print("".join(map(str,[ n//2**i%2 for i in range(int(math.log(n,2)+1)) ][::-1])))

if __name__ == '__main__':
    main()