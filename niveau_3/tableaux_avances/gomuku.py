#!/bin/python3
# -*- coding: utf-8 -*-

# import numpy as np

def isWin(plateau,n):
    lines = []
    for i in range(n):
        lines.append(plateau[i*n:(i+1)*n])
    for j in range(n):
        lines.append("".join([plateau[j+i*n] for i in range(n)]))

    if 4 < n :
        m = (n-5)*2+1#nb of diags
        for k in range(m):#k : no of diag
            v = n-5-abs(k-(n-5))+5#nb of vertices in the diag n°k
            if m // 2 < k :
                lines.append("".join([plateau[(i+k-m//2)*n+n-1-i] for i in range(v)]))
            else:
                lines.append("".join([plateau[i*n+4+k-i] for i in range(v)]))
        for k in range(m):#k : no of diag
            v = n-5-abs(k-(n-5))+5#nb of vertices in the diag n°k
            if m // 2 < k :
                lines.append("".join([plateau[(i+k-m//2)*n+0+i] for i in range(v)]))
            else:
                lines.append("".join([plateau[i*n+n-5-k+i] for i in range(v)]))
    winner = 0
    for l in lines:
        if "11111" in l :
            winner = 1
        elif "22222" in l :
            winner = 2

def isWin3(plateau):
    n = len(plateau)
    matrix = np.array(plateau)
    lines = []
    for i in range(n):
        lines.append(plateau[i])
    for j in range(n):
        lines.append([plateau[i][j] for i in range(n)])

    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))
    lines += [n.tolist() for n in diags if 4 < n.size]

    for l in lines:
        lStr = "".join(map(str,l))
        if "11111" in lStr :
            return 1
        elif "22222" in lStr :
            return 2
    return 0

def isWin4(plateau):
    n = len(plateau)
    lines = []
    for i in range(n):
        lines.append("".join(plateau[i]))
    for j in range(n):
        lines.append("".join([plateau[i][j] for i in range(n)]))

    #SO -> NE
        #lower part, from up
        #upper part, from right
    #NO -> SE
        #lower part, from down
        #upper part, from right
    for k in range(n-1):
        lines.append("".join([plateau[k-d][d] for d in range(k+1)]))
        lines.append("".join([plateau[-1-d][-1-k+d] for d in range(k+1)]))
        lines.append("".join([plateau[-1-k+d][d] for d in range(k+1)]))
        lines.append("".join([plateau[d][-1-k+d] for d in range(k+1)]))
    #main diags
    lines.append("".join([plateau[d][d] for d in range(n)]))
    lines.append("".join([plateau[d][-1-d] for d in range(n)]))

    print(lines)

    for l in lines:
        if "11111" in l :
            return 1
        elif "22222" in l :
            return 2
    return 0

def main():
    n = int(input())
    # plateau = "".join([ input().replace(' ','') for _ in range(n) ])
    plateau = [ input().replace(' ','') for _ in range(n) ]
    # plateau = [ map(int,input().split(' ')) for _ in range(n) ]

    # print(isWin("".join(plateau),n))
    # print(isWin3(plateau))
    print(isWin4(plateau))

if __name__ == '__main__':
    main()