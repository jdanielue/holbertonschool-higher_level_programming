#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        contador = 0
        nuevo_string = ""
        for elemento in my_list:
                if contador < x:
                        nuevo_string += elemento
                contador += 1
        return contador
