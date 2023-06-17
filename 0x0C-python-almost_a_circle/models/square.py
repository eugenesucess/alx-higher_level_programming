#!usr/bin/python3
"""
Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this square class inherit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        """returns dictionary presentation of the rectangle"""
        return {'id': self.id, 'x': self.x, 'size': self.height, 'y': self.y}

    def __str__(self):
        """return string presantation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"