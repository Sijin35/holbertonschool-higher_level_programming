#!/usr/bin/python3
"""Module that inherits from list"""


class MyList(list):
    """Class that inherits from a list"""

    def print_sorted(self):
        """Public instance method that prints sorted list """

        return sorted(self)
