#!/usr/bin/python3
"""Module that writes and returns the number of character return"""


def write_file(filename="", text=""):
    """Function that writes a string and returns
    the number of character written"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
