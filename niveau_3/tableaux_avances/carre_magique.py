#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    carre = []
    for _ in range(n):
        carre.append(list(map(int,input().split(' '))))

    if [ i+1 for i in range(n**2) ] == sorted([ carre[k//n][k%n] for k in range(n**2) ]) :
        sums = [0] * ( n * 2 + 2 )
        for i in range(n):
            sums[i] = sum(carre[i])
        for j in range(n):
            sums[n+j] = sum([carre[i][j] for i in range(n)])
        sums[2*n] = sum([carre[k][k] for k in range(n)])
        sums[2*n+1] = sum([carre[-k-1][k] for k in range(n)])

        isOk = True
        for i in range(len(sums)-1):
            if sums[i] != sums[-1]:
                isOk = False
                break
    else:
        isOk = False

    if isOk:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()