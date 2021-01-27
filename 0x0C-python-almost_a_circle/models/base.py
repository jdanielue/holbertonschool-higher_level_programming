#!/usr/bin/python3
""" new class Base """


class Base():
    """ new class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructo for class Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ writes the JSON string representation of list_objs"""
        import json
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs"""
        import json
        list_dict = []
        for element in list_objs:
            list_dict += [element.to_dictionary()]
        with open("{}.json".format(cls.__name__), "w") as f:
            json.dump(list_dict, f)
