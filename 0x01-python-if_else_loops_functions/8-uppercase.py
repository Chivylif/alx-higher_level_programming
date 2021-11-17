#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord('a') <= ord(x) <= ord('z'):
            print(chr(ord(x) - 32), end="")
        else:
            print(x, end="")
