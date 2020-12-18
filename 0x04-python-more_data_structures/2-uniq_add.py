#!/usr/bin/python3
def uniq_add(my_list=[]):
        uniquelist = set(my_list)
        x = 0
        for i in uniquelist:
                x = x + i
        return x
