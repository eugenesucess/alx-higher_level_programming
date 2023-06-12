#!/usr/bin/python3
"""
MyClass class inherit from list class
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
