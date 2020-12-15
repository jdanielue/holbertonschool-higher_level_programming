#!/usr/bin/env python3
def no_c(my_string):
    strm = ""
    for x in my_string:
        if x != "C" and x != "c":
                strm += x
    return strm
