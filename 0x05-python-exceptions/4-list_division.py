#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nueva_lista = []
    for numero in range(list_length):
        try:
            nuevo_elemento = my_list_1[numero]/my_list_2[numero]
        except ZeroDivisionError:
            print("division by 0")
            nuevo_elemento = 0
        except TypeError:
            print("wrong type")
            nuevo_elemento = 0
        except IndexError:
            print("out of range")
            nuevo_elemento = 0
        finally:
            nueva_lista += [nuevo_elemento]
    return nueva_lista
