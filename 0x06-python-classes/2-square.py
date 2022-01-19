#!/usr/bin/python3
"""Definition of the class Square"""


class Square:
    """An object called Square"""
    pass

    def __init__(self, size=0):
        """Initialize the data"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
