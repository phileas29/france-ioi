#!/bin/python3
# -*- coding: utf-8 -*-

def main():
  alpha = input().lower()
  ss=input()
  s=ss.lower()
  for i,c in enumerate(s):
    if 'a' <= c and c <= 'z':
      if 'a' <= ss[i] and ss[i] <= 'z':
        print(alpha[ord(c)-ord('a')],end='')
      else:
        print(alpha[ord(c)-ord('a')].upper(),end='')
    else:
      print(c,end='')
                

if __name__ == '__main__':
    main()