#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    plateau = []
    for _ in range(8):
        plateau.append(input())

    posChecks = [
        [-2,1],[-1,2],[1,2],[2,1],
        [-2,-1],[-1,-2],[1,-2],[2,-1]
    ]
    posCavaliers = []
    for i,l in enumerate(plateau):
        if 'C' in l:
            posCavaliers.append([l.index('C'),i])
    posDest = [0,0]
    isOk = False
    for posCavalier in posCavaliers:
        for posCheck in posChecks:
            posDest[0] = posCavalier[0] + posCheck[0]
            posDest[1] = posCavalier[1] + posCheck[1]
            if 0 <= posDest[0] and posDest[0] < 8 and \
                0 <= posDest[1] and posDest[1] < 8 and \
                plateau[posDest[1]][posDest[0]].islower() and \
                plateau[posDest[1]][posDest[0]].isalpha() :
                isOk = True
                break

    if isOk:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()