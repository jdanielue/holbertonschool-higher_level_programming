#!/usr/bin/python3
""" This module has the definition of  a Square class"""


class Square():
    """ Model of a square """
    def __init__(self, size=0):
        """ Constructor for Square Method """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of a square """
        area = self.__size ** 2
        return area
