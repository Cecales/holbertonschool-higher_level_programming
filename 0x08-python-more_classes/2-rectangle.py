#!/usr/bin/python3
"""
Module for representation of class rectangle
"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get rectangle width"""
        return self.__width

    @property
    def height(self):
        """get rectangle heigth"""
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
        return (self.__width * 2) + (self.__height * 2)
