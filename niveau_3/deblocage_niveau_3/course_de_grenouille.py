#!/bin/python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input())
    nb = int(input())
    ranking = [0] * n
    finalRanking = [0] * n

    for _ in range(nb-1):
        d = list(map(int,input().split(' ')))
        ranking[d[0]-1] += d[1]
        s = [ e for e in ranking if e == max(ranking) ]
        if len(s) == 1 :
            finalRanking[ranking.index(s[0])] += 1

    print(finalRanking.index(max(finalRanking))+1)