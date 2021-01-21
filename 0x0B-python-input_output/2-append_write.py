#!/usr/bin/python3
"""[ function that write a text file (UTF8)]"""


def append_write(filename="", text=""):
    """[ function that write a text file (UTF8)]"""
    with open(filename, "a", encoding='utf-8') as file:
        text = str(text)
        return file.write(text)
