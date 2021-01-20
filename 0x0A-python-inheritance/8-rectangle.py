#!/usr/bin/python3
"""[empty class BaseGeometry]"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """[class rectangle]"""
    def __init__(self, width, height):
        """[constructor new class]"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
