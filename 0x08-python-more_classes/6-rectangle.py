#!/usr/bin/python3
"""
Module for representation of class rectangle
"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get rectangle width"""
        return self.__width

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        returns a string representation of a rectangle
        instance, filled with the '#' character
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        d_rec = ''
        for i in range(self.__height):
            for j in range(self.__width):
                d_rec += '#'
            if i != self.__height - 1:
                d_rec += '\n'
        return d_rec

    def __repr__(self):
        """
        Return a string representation of a rectangle instance
        using a new instance with eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
