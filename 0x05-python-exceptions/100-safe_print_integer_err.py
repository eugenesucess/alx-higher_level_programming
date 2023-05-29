#!/usr/bin/python3
import sys
def safe_print_integer(value):
    try:
        sys.stderr.write("{:d}".format(value))
        print("\n")
    except (TypeError, ValueError):
        return False
    return True
