#!/usr/bin/python3
"""Definition of the class Square"""


class Square:
    """An object called Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size data"""
        self.size = size
        """Initializes the position data"""
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position to a value"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Initialize the area data"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a figure of a square with the # character"""
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
