#!usr/bin/python3
"""
Rectangle class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """this class inherit from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, valuePased):
        if type(valuePased) != int:
            raise TypeError("width must be an integer")
        if valuePased <= 0:
            raise ValueError("width must be > 0")
        self.__width = valuePased

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, valuePased):
        if type(valuePased) != int:
            raise TypeError("height must be an integer")
        if valuePased <= 0:
            raise ValueError("height must be > 0")
        self.__height = valuePased

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valuePased):
        if type(valuePased) != int:
            raise TypeError("x must be an integer")
        if valuePased < 0:
            raise ValueError("x must be >= 0")
        self.__x = valuePased

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valuePased):
        if type(valuePased) != int:
            raise TypeError("yidth must be an integer")
        if valuePased < 0:
            raise ValueError("y must be >= 0")
        self.__y = valuePased

    def area(self):
        """return the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """print the rectangle in form of #"""
        [print("") for i in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for i in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def update(self, *args):
        """
        it assigns argument to each attribute
        1st arg = id
        2nd arg = widht
        3rd  arg = heihgt
        4th arg = x
        5th arg = y
        """

    def to_dictionary(self):
        """returns dictionary presentation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return string presantation of the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
