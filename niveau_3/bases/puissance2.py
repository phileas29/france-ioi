#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    n = int(sys.stdin.readline())

    print(2**int(math.log(n,2)))

if __name__ == '__main__':
    main()