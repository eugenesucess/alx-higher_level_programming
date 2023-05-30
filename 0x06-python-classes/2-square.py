#!/usr/bin/python3

""" Creation of square class that has size as its private variable"""


class Square:
    """ Initialization of class with init"""
    def __init__(self, size=0):
        try:
          self.__size = size
        except TypeError:
          print("size must be an integer")
        except ValueError:
          print("size must be >= 0")
