#!/usr/bin/python3
"""
add all arguments to the list
"""
import sys

save_to_json_file = \
    __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
items.extend(args[1:])
save_to_json_file(items, "add_item.json")
