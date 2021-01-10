#!/usr/bin/python3
"""[function that prints <first name> <last name>]
"""


def say_my_name(first_name, last_name=""):
    """[ function that prints <first name> <last name>]

    Args:
        first_name ([type]): [description]
        last_name (str, optional): [description]. Defaults to "".
    """

    if type(first_name) == int:
        raise TypeError("first_name must be a string")
    if type(last_name) == int:
        raise TypeError("last_name must be a string")
    
    if first_name == "":
        raise TypeError("first_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
