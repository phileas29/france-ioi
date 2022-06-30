#!/bin/python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    strInput = input()
    dataInput = strInput.split(' ')
    nbLivres = int(dataInput[0])
    nbJours = int(dataInput[1])
    data = []

    nbTotalClients = 0

    for _ in range(nbJours):
        data.append([])
        n = int(input())
        nbTotalClients += n
        for __ in range(n):
            strInput = input().split(' ')
            data[-1].append([ int(e) for e in strInput ])

    # data = [
    #     [
    #         [
    #             [0,3],
    #             [1,3]
    #         ]
    #     ]
    # ]

    availability = [ 0 for _ in range(nbTotalClients) ]

    for day in data:
        for book in day:
            if availability[book[0]] == 0 :
                print("1")
                availability[book[0]] = book[1]
            else:
                print("0")

        for i in range(len(availability)):
            if 0 < availability[i] :
                availability[i] -= 1
