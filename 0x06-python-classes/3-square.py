#!/usr/bin/python3
""" This module has the definition of  a Square class"""


class Square():
    """ Model of a square """
    def __init__(self, size=0):
        """ Constructor for Square Method """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area of a square """
        area = self.__size ** 2
        return area
