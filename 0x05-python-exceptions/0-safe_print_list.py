#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_element = ""
    contador = 0
    for elemento in my_list:
        if contador < x:
            try:
                new_element += elemento
            except TypeError:
                new_element += str(elemento)
            contador += 1
    print(new_element)
    return contador
