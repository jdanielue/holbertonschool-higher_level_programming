#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "x", encoding='utf-8') as file:
        text = str(text)
        return file.write(text)
