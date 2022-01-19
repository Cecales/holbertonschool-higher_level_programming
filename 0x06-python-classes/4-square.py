#!/usr/bin/python3
"""Definition of the class Square"""


class Square:
    """An object called Square"""
    def __init__(self, size=0):
        """Initialize the size data"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Initialize the area data"""
        return (self.__size * self.__size)
