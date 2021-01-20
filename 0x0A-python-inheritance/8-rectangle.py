#!/usr/bin/python3
"""[empty class BaseGeometry]"""


class BaseGeometry():
    """[empty class BaseGeometry]"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """[nteger validator]"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """[empty class rectangle]"""
    def __init__(self, width, height):
        """[constructor new class]"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
