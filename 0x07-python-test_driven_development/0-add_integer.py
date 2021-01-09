#!/usr/bin/python3
"""[modulo punto 0]
Raises:
    TypeError: [a must be an integer]
    TypeError: [b must be an integer]
Returns:
    [type]: [sum]
"""""


def add_integer(a, b=98):
    """[summary]
    Args:
        a ([type]): [first number]
        b (int, optional): [second number]. Defaults to 98.
    Raises:
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]
    Returns:
        [type]: [description]
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
