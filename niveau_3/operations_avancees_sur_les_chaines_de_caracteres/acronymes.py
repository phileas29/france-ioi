#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    acr=input().lower()
    n=int(input())
    l=[]
    ko = False
    for _ in range(n):
        l.append(input().lower().split(' '))
    for i in range(len(l)):
        if len(acr) == len(l[i]):
            for j in range(len(l[i])):
                if l[i][j][0] != acr[j] :
                    ko = True
                    break
            if not ko :
                for j in range(len(l[i])):
                    print(l[i][j].capitalize()+' ',end='')
                print()
            ko = False
                

if __name__ == '__main__':
    main()