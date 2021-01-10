#!/usr/bin/python3
"""[module point 1]
Raises:
    TypeError: [a must be an integer]
    TypeError: [b must be an integer]
Returns:
    [type]: [sum]
"""""


def matrix_divided(matrix, div):
    """[function that divides all elements of a matrix]

    Args:
        matrix ([list]): [matrix ]
        div ([integer]): [number to be divideed]
    """

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    mat_div = []
    for row in matrix:
        dato = []
        for column in row:
            if type(column) != int and type(column) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            dato += [round((column / div), 2)]
        mat_div += [dato]

    for fila in matrix:
        largo = len(fila)
        for fila2 in matrix:
            if largo != len(fila2):
                raise TypeError("Each row of the matrix must have the\
 same size")

    return mat_div
