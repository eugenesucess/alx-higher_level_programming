#!/usr/bin/pyton3
"""
class rectangle that defines a rectangle
"""


class Rectangle:
    """ defines a rectangle with w and l """
    def __init__(self, width=0, height=0):
        """ initialize rectangle """
        self.width = width
        self.height = height

    @property
    def width(self, width=0, height=0):
        """ return private instance """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of the rctnagle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
