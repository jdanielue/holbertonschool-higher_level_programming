#!/usr/bin/python3
"""[empty class Rectangle that defines a rectangle]"""


class Rectangle():
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """[empty class Rectangle that defines a rectangle]

        Args:
            width (int, optional): [description]. Defaults to 0.
            height (int, optional): [description]. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            perimetro = 0
        else:
            perimetro = (self.width * 2) + (self.height * 2)
        return perimetro

    def __str__(self):
        hash = "#"
        forma = ""
        if self.width == 0 or self.height == 0:
            return forma
        for renglon in range(0, self.height):
            if renglon != self.height - 1:
                forma += hash * self.width
                forma += "\n"
            else:
                forma += hash * self.width
        return forma

    def __repr__(self) -> str:
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
