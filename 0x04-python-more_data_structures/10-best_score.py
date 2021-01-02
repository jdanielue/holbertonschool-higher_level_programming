#!/usr/bin/python3
def best_score(a_dictionary):
    mayor = 0
    retorno = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    for comparado in a_dictionary.items():
        if len(a_dictionary) == 1:
            return comparado[0]
        if comparado[1] > mayor:
            mayor = comparado[1]
            retorno = comparado[0]
    return retorno
