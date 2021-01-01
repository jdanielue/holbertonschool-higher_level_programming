#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for ch in range(0, len(str)):
        if ch == n:
            continue
        newstr += str[ch]
    return newstr
