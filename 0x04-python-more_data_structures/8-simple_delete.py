#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    check = 0;

    for keys in a_dictionary.keys():
        if keys == key:
            check += 1

    if check > 0:
        del a_dictionary[key]
    return a_dictionary
