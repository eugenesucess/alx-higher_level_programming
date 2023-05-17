#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    #holder = []
    #listOfValues = list(a_dictionary.values())
    #for i in listOfValues:
       #holder.append(i * 2)
    #newDict = dict(zip(list(a_dictionary.keys()), holder))
    #return newDict    new_dictionary = {}
    for key in a_dictionary:
        new_dictionary.update({key: a_dictionary.get(key) * 2})
    return new_dictionary
