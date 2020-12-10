#!/usr/bin/python3
def uppercase(str):
    strm = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            strm += chr(ord(str[i]) - 32)
        else:
            strm += str[i]
    print(strm)
