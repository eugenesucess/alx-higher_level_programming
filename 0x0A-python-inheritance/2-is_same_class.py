#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ returns true if the object passed as arg is the same type"""
    if type(obj) is a_class:
        return True
    return False
