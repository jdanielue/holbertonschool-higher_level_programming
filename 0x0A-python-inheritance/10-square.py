#!/usr/bin/python3
"""[empty class BaseGeometry]"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
    """[empty class rectangle]"""
    def __init__(self, size):
        """[constructor new class]"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
