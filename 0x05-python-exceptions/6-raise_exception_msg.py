#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        4 + spam*3
    except NameError:
        print(message)
