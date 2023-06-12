#!/usr/bin/python3
"""
inherit BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation of a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.height = height
