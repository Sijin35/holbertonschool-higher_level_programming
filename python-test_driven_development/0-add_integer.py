#!/usr/bin/python3
"""

Module that adds 2 integers
"""


def add_integer(a, b=98):
    """

    Function that retruns the addition of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    res_1 = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    res_2 = int(b)
    return res_1 + res_2
