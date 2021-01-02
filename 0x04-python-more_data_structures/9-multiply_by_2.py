#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for num, llave in zip(a_dictionary.values(), a_dictionary.keys()):
        new_dictionary[llave] = num * 2
    return new_dictionary
