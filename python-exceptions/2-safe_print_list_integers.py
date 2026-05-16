#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{}".format(my_list[i]), end="")
                c += 1
        except (IndexError, ValueError):
            break
    print()
    return c
