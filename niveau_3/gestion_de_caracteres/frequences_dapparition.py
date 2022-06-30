#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = input().lower()
    ss = [ s[i] for i in range(len(s)) if s[i] in alphabet ]
    for c in alphabet :
        print(float(ss.count(c))/len(ss))
    
if __name__ == '__main__':
    main()