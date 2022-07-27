#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    tab = [ input() for _ in range(n) ]

    for r in sorted(tab):
        print(r)

if __name__ == '__main__':
    main()