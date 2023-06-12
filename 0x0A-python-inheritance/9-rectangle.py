#!/usr/bin/python3
"""
inherit BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry to have access"""

    def __init__(self, width, height):
        """Instantiation of a new Rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.height = height

        def area(self):
            """returns the area of the rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """ return to a descripcion about this class"""
            return ("[Rectangle] {}/{}".format(self.__width, self.__height))
