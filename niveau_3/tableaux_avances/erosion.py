#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    # trans = { '.' : 0 , '#' : 1 }
    n = int(input())
    dim = [ int(x) for x in input().split(' ') ]
    imageA = [ [ c for c in input() ] for i in range(dim[0]) ]
    imageB = [ [ c for c in imageA[i] ] for i in range(len(imageA)) ]

    for k in range(n):
        for i in range(dim[0]):
            for j in range(dim[1]):
                if i == 0 or j == 0 or i == dim[0]-1 or j == dim[1]-1 :
                    imageB[i][j] = '.'
                else:
                    if imageA[i+1][j] == '#' and imageA[i-1][j] == '#' and \
                        imageA[i][j+1] == '#' and imageA[i][j-1] == '#' :
                        imageB[i][j] = '#'
                    else:
                        imageB[i][j] = '.'
        for i in range(dim[0]):
            for j in range(dim[1]):
                imageA[i][j] = imageB[i][j]

    for i in range(dim[0]):
        print("".join(imageB[i]))

if __name__ == '__main__':
    main()