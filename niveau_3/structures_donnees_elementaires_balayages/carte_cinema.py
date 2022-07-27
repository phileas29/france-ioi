#!/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    ids = [ int(id) for id in sys.stdin.readline().split(' ') ]

    idsSorted = sorted(ids)
    duplicates = []
    for i in range(1,len(idsSorted)):
        if idsSorted[i-1] == idsSorted[i] :
            duplicates.append(idsSorted[i])

    if 1 < len(duplicates):
        indexIdsDuplicated = []
        for id in duplicates:
            indexTmp = ids.index(id)+1
            indexIdsDuplicated.append(ids[indexTmp:].index(id)+indexTmp)
        print(ids[min(indexIdsDuplicated)])
    elif len(duplicates) == 1:
        print(duplicates[0])
    else:
        print(-1)

if __name__ == '__main__':
    main()