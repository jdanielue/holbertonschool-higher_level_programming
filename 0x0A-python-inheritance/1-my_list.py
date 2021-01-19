#!/usr/bin/python3
"""[Write a class MyList that inherits from list]"""


class MyList(list):
    """[Write a class MyList that inherits from list]
    Args:
        list ([type]): [description]
    """

    def print_sorted(self):
        print(sorted(self))
