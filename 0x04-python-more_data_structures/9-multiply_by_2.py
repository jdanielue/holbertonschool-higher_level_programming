#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for llave in a_dictionary:
        new_dictionary[llave] = a_dictionary[llave] * 2
    return new_dictionary