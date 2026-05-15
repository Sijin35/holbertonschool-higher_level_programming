#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    new = my_list[:]
    return list(map(lambda i: i * number, new))
