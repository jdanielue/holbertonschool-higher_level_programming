#!/usr/bin/python3
"""class Rectangle that inherits from Base"""


Base = __import__("models.base", fromlist=[None]).Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor class Rectangle that inherits from Base"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ clss method that return the area of a rectangle"""
        return self.height * self.width

    def display(self):
        """ clss method that return the shape of a rectangle"""
        forma = ""
        print_symbol = "#"
        counter_x = 0
        if self.width == 0 or self.height == 0:
            return forma
        forma += "\n" * self.y
        for renglon in range(0, self.__height):
            if self.x > 0:
                forma += "_" * self.x
            if renglon != self.__height - 1:
                forma += print_symbol * self.width
                forma += "\n"
            else:
                forma += print_symbol * self.width
        print(forma)

    def __str__(self):
        """ clss method that return the str rep of a rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """ clss method that return the update of a rectangle"""
        attributes = ["id", "width", "height", "x", "y"]
        dict_att = {'id': self.id, 'width': self.width, 'height': self.height
                    'x': self.x, 'y': self.y}
        if args and len(args) != 0:
            for element, att in zip(attributes, args):
                setattr(self, element, att)
        else:
            for element_key, values in kwargs.items():
                if element_key in dict_att:
                    setattr(self, element_key, values)

    def to_dictionary(self):
        """ clss method that return the dictionary of a rectangle"""
        new_dict = self.__dict__.copy()
        for old_key, value in self.__dict__.items():
            new_key = old_key.replace("_Rectangle__", "")
            new_dict[new_key] = self.__dict__[old_key]
            new_dict.pop(old_key)
        return new_dict
