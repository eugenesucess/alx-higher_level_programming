#!usr/bin/python3
"""
parent class Bas
"""
import json


class Base:
    """
    Base class with private class attribute
    To change class attribute we will need to use
    Base.(attribute name)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """loop through passed list to see if there is only dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) is list:
            for dictionaries in list_dictionaries:
                if type(dictionaries) is not dict:
                    return "[]"
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        dictionaries = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for lists in list_objs:
                dictionaries.append(lists.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        if json_string.__class__ is str:
            return json.loads(json_string)
