#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    for n in keys:
        if value == a_dictionary.get(n):
            del a_dictionary[n]
    return (a_dictionary)
