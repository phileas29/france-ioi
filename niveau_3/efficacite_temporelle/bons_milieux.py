#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def getMiddle(p1,p2):
    m = [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    if m[0].is_integer() and m[1].is_integer():
        return [ int(e) for e in m ]
    else:
        return None

def main():
    map1 = [ [ 0 for j in range(101) ] for i in range(101) ]
    n = int(sys.stdin.readline())
    points = []
    for _ in range(n):
        points.append([ int(e) for e in sys.stdin.readline().split(' ')[:2] ])
        map1[points[-1][0]][points[-1][1]] = 1

    points.sort()
    
    nbMedianPoints = 0
    for i in range(1,len(points)):
        for j in range(i):
            m = getMiddle(points[i],points[j])
            if m != None and map1[m[0]][m[1]] == 1 :
                nbMedianPoints += 1
                map1[m[0]][m[1]] = 2

    nbMedianPoints = 0
    for i in range(1,len(points)):
        for j in range(i):
            m = getMiddle(points[i],points[j])
            if m != None and map1[m[0]][m[1]] == 1 :
                nbMedianPoints += 1
                map1[m[0]][m[1]] = 2

    print(nbMedianPoints)

if __name__ == '__main__':
    main()