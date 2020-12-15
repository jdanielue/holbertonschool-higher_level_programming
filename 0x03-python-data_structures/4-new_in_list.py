#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list):
        return (my_list)
    if idx < 0:
        return (my_list)
    nueva_lista = my_list[:]
    nueva_lista[idx] = element
    return nueva_lista