#!/usr/bin/python3
"""[resumennumero 2]
"""

def print_square(size):
    """[resumen de lo que estoy haciendo]

    Args:
        size ([type]): [description]
    """
    hash = "#"

    if type(size) != int:
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for len in range(size):
        print("{}".format(hash * size))