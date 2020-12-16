#!/usr/bin/python3
def divisible_by_2(my_list=[]):
        listavf = []
        for i in my_list:
                if i % 2 == 0:
                        listavf += [True]
                else:
                        listavf += [False]
        return listavf
