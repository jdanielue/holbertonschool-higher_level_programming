#!/usr/bin/python3
def best_score(a_dictionary):
    mayor = list()
    if a_dictionary is None:
        return None
    for actual in a_dictionary.items():
        for comparado in a_dictionary.items():
            if actual[1] < comparado[1]:
                mayor = comparado[0]

    return mayor
