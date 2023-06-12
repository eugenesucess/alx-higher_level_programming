#!/usr/bin/python3
"""
MyClass class inherit from list class
"""


class MyList(list):
    def print_sprted(self):
        for i in range(len(list)):
            if not isinstance(list[i], int):
                return None
             if list[i] > list[i + 1]:
                  bigN = list[i]
                  list[i] = list[i + 1]
                  list[i + 1] = bigN
