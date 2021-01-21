#!/usr/bin/python3
"""[ function that write a text file (UTF8)]"""
def write_file(filename="", text=""):
    """[ function that write a text file (UTF8)]"""
    with open(filename, "x", encoding='utf-8') as file:
        text = str(text)
        return file.write(text)
