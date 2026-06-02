#!/usr/bin/python3
"""Module that appends a string and returns the number of characters added"""


def append_write(filename="", text=""):
    """Function that appends string at end of text file and
    returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
