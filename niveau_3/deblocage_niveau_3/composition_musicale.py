#!/bin/python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input()
    goOut = False
    while not goOut:
        goOut = True
        for i in range(len(sentence)-1):
            if sentence[i] == sentence[i+1] :
                sentence = sentence.replace(sentence[i:i+2],'')
                goOut = False
                break
    print(sentence)
