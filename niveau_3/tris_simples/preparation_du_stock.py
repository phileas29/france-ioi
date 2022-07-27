#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    p = [ int(e) for e in input().split(' ') ]
    stock = [ int(e) for e in input().split(' ')[:p[0]] ]
    mustBeInserted = [ int(e) for e in input().split(' ')[:p[1]] ]
    indexInsertions = []
    
    for i in range(len(mustBeInserted)):
        for j in range(len(stock)+1):
            if j == len(stock) or mustBeInserted[i] <= stock[j]:
                indexInsertions.append(j)
                stock.insert(j,mustBeInserted[i])
                break

    print(" ".join(map(str,indexInsertions)))
    print(" ".join(map(str,stock)))


if __name__ == '__main__':
    main()