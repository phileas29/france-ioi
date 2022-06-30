#!/bin/python3
# -*- coding: utf-8 -*-

def main():
    s = ord(input()[0]) - 64
    age = chr(64+int(input()))
    print(str(s)+age)

if __name__ == '__main__':
    main()