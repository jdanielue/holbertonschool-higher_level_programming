#!/usr/bin/env python3
def no_c(my_string):
    strmo = ""
    for x in my_string:
        if x != "C" and x != "c":
                strmo += x
    return strmo
