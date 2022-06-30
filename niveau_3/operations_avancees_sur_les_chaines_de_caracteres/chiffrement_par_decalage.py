#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    n=int(input())-1
    l=[""]*n
    for i in range(n):
        l[i] = input()

    for i in range(n):
        d = 3*(i+2)*((i+1)%2)-5*(i+2)*(i%2)
        for j in range(len(l[i])):
            if l[i][j].isalpha() :
                if l[i][j].islower():
                    print(chr((ord(l[i][j].lower())-ord('a')-d)%26+ord('a')),end='')
                else:
                    print(chr((ord(l[i][j].lower())-ord('a')-d)%26+ord('a')).upper(),end='')
            else:
                print(l[i][j],end='')
        print()

if __name__ == '__main__':
    main()