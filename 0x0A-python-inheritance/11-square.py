#!/usr/bin/python3
"""Defines square as subclass of rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square use rectangle instances."""

    def __init__(self, size):
        """Initialize a square(new)."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """Return the area frm rectangle"""
        return self.size * self.__size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.size) + "/" + str(self.size)
        return string
