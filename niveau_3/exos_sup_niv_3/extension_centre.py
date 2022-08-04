#!/bin/python3
# -*- coding: utf-8 -*-

import sys, math

def main():
    n = int(sys.stdin.readline(),16)
    
    print(hex(int(sum([ int(sys.stdin.readline(),16) for i in range(n) ])/n))[2:].upper())

if __name__ == '__main__':
    main()