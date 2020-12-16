#!/usr/bin/python3
def max_integer(my_list=[]):
        if my_list == []:
                return None
        temporal = my_list[0]
        for i in my_list:
                if i > temporal:
                        temporal = i
        return temporal
