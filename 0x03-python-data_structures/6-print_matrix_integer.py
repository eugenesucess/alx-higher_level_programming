#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for values in row:
            print("{:d}".format(values), end=" ")
        print()
