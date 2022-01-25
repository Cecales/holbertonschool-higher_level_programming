#!/usr/bin/python3
"""
Module for representation of class rectangle
"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, heigth=0):
        """Initializes a rectangle instance"""
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        """get rectangle width"""
        return self.__width

    @property
    def heigth(self):
        """get rectangle heigth"""
        return self.__heigth

    @width.setter
    def width(self, value):
        """set rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @heigth.setter
    def heigth(self, value):
        """set rectangle height"""
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value <= 0:
            raise ValueError("heigth must be > 0")
        self.__heigth = value

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__heigth

    def perimeter(self):
        """perimeter of the rectangle"""
        return (self.__width * 2) + (self.__heigth * 2)
