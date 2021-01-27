#!/usr/bin/python3
"""class square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor class Square that inherits from Rectangle """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """ clss method that return the str rep of a rectangle"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """ clss method that return the str rep of a rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """ clss method that return the str rep of a rectangle"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ clss method that return the update of a square"""
        attributes = ["id", "size", "x", "y"]
        dict_kwargs = {'id': self.id, 'size': self.width,
                       'x': self.x, 'y': self.y}
        if args and len(args) != 0:
            for element, att in zip(attributes, args):
                setattr(self, element, att)
        else:
            for element_key, values in kwargs.items():
                if element_key in dict_kwargs:
                    setattr(self, element_key, values)

    def to_dictionary(self):
        """ clss method that return the dictionary of a square"""
        new_dict = self.__dict__.copy()
        for old_key, value in self.__dict__.items():
            if "_Rectangle__" not in old_key:
                continue
            new_key = old_key.replace("_Rectangle__", "")
            new_dict[new_key] = self.__dict__[old_key]
            new_dict.pop(old_key)
        new_dict["size"] = self.width
        new_dict.pop("width")
        new_dict.pop("height")
        return new_dict
