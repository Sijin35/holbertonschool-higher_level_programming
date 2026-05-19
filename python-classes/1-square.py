#!/usr/bin/python3
"""Defines a square with private attribute size."""


class Square:
    """Represents a square with private attribute size."""
    
    def __init__(self, size=0):
        """Initializes a square with private attribute size."""
        
        self.__size = size
