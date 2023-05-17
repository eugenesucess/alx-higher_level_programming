#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortThem = dict(sorted(a_dictionary.items()))
    for i, j in sortThem.items():
        print("{} : {}".format(i, j))
