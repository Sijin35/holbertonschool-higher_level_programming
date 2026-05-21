#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res =  a / b
    except (ZeroDivisionError):
        print("Inside result: {}".format(None))
        return None
    finally:
        print("Inside result: {}".format(a / b))
    return res
