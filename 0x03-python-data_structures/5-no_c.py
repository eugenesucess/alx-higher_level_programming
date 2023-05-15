#!/usr/bin/env python3
def no_c(my_string):
    newStr = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            newStr += my_string[i]
    return newStr
