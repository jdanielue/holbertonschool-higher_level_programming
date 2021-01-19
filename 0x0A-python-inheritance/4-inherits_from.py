#!/usr/bin/python3
"""True if the object is an instance"""


def inherits_from(obj, a_class):
    """True if the object is an instance"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
