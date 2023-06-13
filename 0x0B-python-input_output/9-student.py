#!/usr/bin/python3
"""
return dict represantation of self class
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """returns __dict__"""
        return self.__dict__
