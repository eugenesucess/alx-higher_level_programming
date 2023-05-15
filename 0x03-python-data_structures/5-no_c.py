#!/usr/bin/env python3
def no_c(my_string):
    newStr = {99:None}
    nz = {67:None}
    newest =  my_string.translate(newStr)
    rsStr = newest.translate(nz)
    return rsStr
