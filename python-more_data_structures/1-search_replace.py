#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = my_list[:]
    for i, v in enumerate(my_list):
        if v == search:
            new[i] = replace
    return new
# new = [replace if i == search else i for i in my_list] 
# List comprehension if want to use
