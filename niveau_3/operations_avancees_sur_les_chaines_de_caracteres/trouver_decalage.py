#!/bin/python3
# -*- coding: utf-8 -*-

#pour d=11
#E=abcdefghijklmnopqrstuvwxyz
#F=pqrstuvwxyzabcdefghijklmno
#f:E->F
def decode(s,d):
    sLower = s.lower()
    sDecoded = ['']*len(s)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    dictAlpha = {}
    for i in range(26):
        dictAlpha.update({alpha[i]:alpha[(i-d)%26]})
    for j in range(len(s)):
        if s[j].isalpha() :
            if s[j].islower():
                sDecoded[j]=dictAlpha[sLower[j]]
            else:
                sDecoded[j]=dictAlpha[sLower[j]].upper()
        else:
            sDecoded[j]=s[j]
    return "".join(sDecoded)

def bruteforce(s):
    freqE = []
    l = []
    slow = s.lower()

    for d in range(26):
        l.append(decode(s,d))
        freqE.append(l[-1].lower().count('e'))
    
    print(l[freqE.index(max(freqE))])

def analyse(s):
    sLower = s.lower()
    freqAlpha = [0]*26
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in range(26):
        freqAlpha[i] = sLower.count(alpha[i])

    d = freqAlpha.index(max(freqAlpha))-alpha.index('e')

    print(decode(s,d))

def main():
    s = input()
    # test = "Np epiep fetwtdp fy opnlwlrp op zykp nlclnepcpd."
    # analyse(test)
    # bruteforce(test)
    analyse(s)
    # bruteforce(s)

if __name__ == '__main__':
    main()
