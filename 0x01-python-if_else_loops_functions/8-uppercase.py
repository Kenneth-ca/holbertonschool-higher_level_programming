#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if (ord(s) > 96) and (ord(s) < 123):
            aux = ord(s) - 32
        else:
            aux = ord(s)
        print(chr(aux), end="")
    print("")
