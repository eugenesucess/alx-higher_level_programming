#!/usr/bin/python3
"""
Reads file and print the content on the stdout
"""


def read_file(filename=""):
    """print content of the file passed"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
