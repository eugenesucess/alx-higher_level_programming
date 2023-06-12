#!/usr/bin/python3
"""
shows name of class that it inherits from
"""


def inherits_from(obj, a_class):
    """check if class has inherited frm super class"""
    if ((issubclass(type(obj), a_class)) and (type(obj) is not a_class)):
        return True
