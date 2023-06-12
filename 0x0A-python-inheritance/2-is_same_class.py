#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ returns true if the object passed as arg is the same type as the class"""
    if isintance(obj, a_class):
        return True
    return False
